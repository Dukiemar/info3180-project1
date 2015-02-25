from flask.ext.wtf import Form
from wtforms import StringField, TextField;
from wtforms.validators import DataRequired, Required


class signUp(Form):
  image=TextField('image', validators=[Required()])
  firstname = TextField('firstname', validators=[Required()])
  lastname = TextField('lastname', validators=[Required()])
  age = TextField('age', validators=[Required()])
  sex = TextField('sex', validators=[Required()])
  
	