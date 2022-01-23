import logging

from flask import Flask
from flask_appbuilder import AppBuilder, SQLA

# Logging configuration
logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)

flask_app = Flask(__name__)
flask_app.config.from_object("project.web.config")
flask_db = SQLA(flask_app)
appbuilder = AppBuilder(flask_app, flask_db.session)

from . import views
