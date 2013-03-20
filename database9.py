from flask.ext.sqlalchemy import SQLAlchemy
from flask9 import app

db = SQLAlchemy(app)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return "<Person %s: %s>" % (self.id, self.name)
