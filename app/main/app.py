from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

#sqlalchemy database config, dialect://user:pass@url:port/dbname
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Password123@localhost:5432/template_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
from model import db
ma = Marshmallow(db)

from service.api_service import Service
service = Service(app,db)
from controller.sample_controller import SampleController
sample_controller = SampleController(app,db,service)

if(__name__=='__main__'):
<<<<<<< HEAD
    db.init_app(app)
    app.run(debug=True)
=======
    app.run(debug=True)
>>>>>>> f1389222b87a87bd4ffbda9aa0c41b00bb994174
