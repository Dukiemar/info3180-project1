from flask.ext.wtf import Form
from wtforms import StringField, TextField;
from wtforms.validators import DataRequired, Required




class signUp(Form):
  WTF_CSRF_ENABLED = False
  #SECRET_KEY = 'javanddukes'

  
  image=TextField('Image', validators=[Required()])
  firstname = TextField('First Name', validators=[Required()])
  lastname = TextField('Last Name', validators=[Required()])
	#userid = TextField('ID', validators=[Required()])
  sex = TextField('Sex', validators=[Required()])
  age = TextField('Age', validators=[Required()])
	