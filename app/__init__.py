from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from config import SQLALCHEMY_DATABASE_URI #to remove

app = Flask(__name__)


#app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://action@localhost/action'
#app.config['SECRET_KEY']="javanddukes"
app.config['SQLALCHEMY_DATABASE_URI']="postgresql://vidzrwuyuffrca:QGgNREuw1rdKWvH3JrV1QjiSzY@ec2-107-20-234-127.compute-1.amazonaws.com:5432/d1hnnf2me1878c"
app.config.from_object('config')
db=SQLAlchemy(app)

from app import views, models
