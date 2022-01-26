from flask import render_template, jsonify, request
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi

from . import flask_app, appbuilder, db
from .models import EmailModel

@flask_app.route('/register')
def register_email():
    email_address = request.args.get('email_address', '', type=str)
    print(f'registering: {email_address} ...')
    return jsonify(status=200)

class EmailModelView(ModelView):
    datamodel = SQLAInterface(EmailModel)
    list_columns = ['email_address']

db.create_all()

appbuilder.add_view(
    EmailModelView,
    "List Emails",
    icon = "fa-folder-open-o",
    category = "Emails",
    category_icon = "fa-envelope"
)


# Application wide 404 error handler
@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )
