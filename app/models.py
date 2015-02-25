from . import db

class User(db.Model):
  userid = db.Column(db.Integer, primary_key=True)
  firstname = db.Column(db.String(80), unique=True)
  lastname = db.Column(db.String(120), unique=True)
  age=db.Column(db.String(64),unique=True)
  sex=db.Column(db.String(64),unique=True)
  image=db.Column(db.String(120),unique=True)
  highScore=db.Column(db.Integer,unique=True)
  dollars=db.Column(db.Integer,unique=True)
    
  def __init__(self,firstname,lastname,age,sex,image,highscore,dollars):
    self.firstname = firstname
    self.lastname = lastname
    self.age=age
    self.image=image
    self.highscore=0
    self.dollar=0

  def __repr__(self):
      return '<User %r>' % self.firstname