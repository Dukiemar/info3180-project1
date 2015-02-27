from flask.ext.wtf import Form
from wtforms import StringField, TextField, FileField
from wtforms.validators import DataRequired, Required
from flask_wtf.file import FileField, FileRequired

class signUp(Form):
  image=FileField('image', validators=[Required()])
  firstname = TextField('firstname', validators=[Required()])
  lastname = TextField('lastname', validators=[Required()])
  age = TextField('age', validators=[Required()])
  sex = TextField('sex', validators=[Required()])
  
	