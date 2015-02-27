from . import db


class SignUp(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  image=db.Column(db.String(120))
  firstname = db.Column(db.String(80), unique=True)
  lastname = db.Column(db.String(120), unique=True)
  age=db.Column(db.String(64))
  sex=db.Column(db.String(64))
  highscore=db.Column(db.Integer)
  tdollars=db.Column(db.Integer)
  
    
  def __init__(self,firstname,lastname,age,sex,image):
    self.image=image
    self.firstname = firstname
    self.lastname = lastname
    self.age=age
    self.sex=sex
    self.highscore=0
    self.tdollars=0
  
  def __repr__(self):
      return '<SignUp %r>' % self.firstname

