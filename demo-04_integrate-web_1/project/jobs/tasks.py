"""tasks.py"""
import os
import yaml
import smtplib
import ssl
from typing import List
from email.mime.text import MIMEText
from celery.schedules import crontab

from jobs import celery_app, backend
from jobs.emails import get_recipients

jobs_path = os.path.abspath(os.path.dirname(__file__))

# loading smtp server configuration data 
SMTP_HOST     = None
SMTP_PORT     = None
SMTP_ACCOUNT  = None
SMTP_PASSWORD = None
MESSAGE       = None

config_path = os.path.join(jobs_path, 'res/config.yml')
with open(config_path, 'r', encoding='utf-8') as fp:
    try:
        smtp_config = yaml.safe_load(fp)
    except yaml.YAMLError as yml_err:
        print(str(yml_err))
    else:
        SMTP_HOST     = smtp_config.get('smtp_host')
        SMTP_PORT     = smtp_config.get('smtp_port')
        SMTP_ACCOUNT  = smtp_config.get('smtp_account')
        SMTP_PASSWORD = smtp_config.get('smtp_password')

msg_path = os.path.join(jobs_path, 'res/email_message2.txt')
with open(msg_path, 'r', encoding='utf-8') as fp:
    MESSAGE = fp.read()

from_email = SMTP_ACCOUNT
to_email = get_recipients(backend)

@celery_app.on_after_configure.connect
def send_weekly_notice(sender, **kwargs):

    sender.add_periodic_task(
        crontab(hour=22, minute='50', day_of_week=2),
        email_notification.s(from_email=from_email,
                           to_email=to_email,
                           subject="Happy New Week!!",
                           message=MESSAGE),
    )


@celery_app.task(bind=True)
def email_notification(self, from_email:str, to_email:List[str],
                       subject:str, message:str) -> None:
    msg            = MIMEText(message, 'plain')
    msg['Subject'] = subject
    msg['From']    = from_email
    msg['To']      = ",".join(to_email)
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT, context=context) as smtp_server:
            smtp_server.login(SMTP_ACCOUNT, SMTP_PASSWORD)
            if 'Content-type: text/html' in message:
                smtp_server.sendmail(from_email, to_email, message)
            else:
                smtp_server.sendmail(from_email, to_email, msg.as_string())
    except Exception as err:
        print(str(err))
        return False
    return True

