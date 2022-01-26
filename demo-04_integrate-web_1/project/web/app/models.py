from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class EmailModel(Model):
    """
    the extremely simple data model, it only has one single
    column, which is also primary key
    """
    email_address = Column(String(64), primary_key=True)

    def __repr__(self) -> str:
        return self.email_address
