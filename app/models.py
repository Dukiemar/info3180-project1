from . import db


class Signin(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  image=db.Column(db.String(120),unique=True)
  firstname = db.Column(db.String(80), unique=True)
  lastname = db.Column(db.String(120), unique=True)
  age=db.Column(db.String(64),unique=True)
  sex=db.Column(db.String(64),unique=True)
  
    
  def __init__(self,firstname,lastname,age,sex,image):
    self.image=image
    self.firstname = firstname
    self.lastname = lastname
    self.age=age
    self.sex=sex
  
  

  def __repr__(self):
      return '<User %r>' % self.firstname

