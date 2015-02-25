"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

from app import app
from flask import render_template, request, redirect, url_for
from app import db
from app.models import Signin

from .form import signUp

import os
###
# Routing for your application.
###
WTF_CSRF_ENABLED = False
#SECRET_KEY = 'dukes'

@app.route('/home')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


#if __name__ == '__main__':   
 #app.run(debug=True,host="0.0.0.0",port="8888")
    

  
@app.route('/signup')
def signup():
  return render_template('signup.html')

@app.route('/profile', methods=['GET','POST'])
def profile():
    form=signUp(csrf_enabled=False)
    #import pdb;pdb.set.trace()
    if request.method == 'POST' and form.validate():
      #user=User(request.form['image'],request.form['firstname'],request.form['lastname'] ,request.form['age'], request.form['sex'])
      user=Signin(form.firstname.data, form.lastname.data, form.age.data, form.sex.data,form.image.data)
      #user=User(firstname=firstname,lastname=lastname,age=age,sex=sex,image=image)
      db.session.add(user)
      db.session.commit()  
    return render_template('signup.html',form=form)
    

if __name__ == '__main__':
  app.run(debug=True,host="0.0.0.0",port="8080")


