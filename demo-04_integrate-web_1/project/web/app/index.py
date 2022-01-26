"""index.py"""
from flask_appbuilder import IndexView

class EmailIndexView(IndexView):
    """Override the Index View"""
    index_template = 'index.html'
