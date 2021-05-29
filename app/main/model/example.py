#Example model
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
db = SQLAlchemy()

class Example(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)


    def __init__(self,name) -> None:
        self.name=name



#Example Schema
ma = Marshmallow(db)
class ExampleSchema(ma.Schema):
    class Meta:
        fields = ('id','name')