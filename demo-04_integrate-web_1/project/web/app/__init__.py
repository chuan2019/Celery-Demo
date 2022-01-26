"""__init__.py"""
from flask import Flask
from flask_appbuilder import AppBuilder, SQLA

from project.web.app.index import EmailIndexView

# Creating and Configuring Flask App
flask_app = Flask(__name__)
flask_app.config.from_object("project.web.config")
db = SQLA(flask_app)
appbuilder = AppBuilder(flask_app, db.session, indexview=EmailIndexView)

from . import views
