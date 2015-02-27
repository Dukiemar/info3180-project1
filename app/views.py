"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""
import os
from flask_wtf.file import FileField
from werkzeug import secure_filename
from app import app
from flask import render_template, request, redirect, url_for,send_file,flash
from app import db
from app.models import SignUp
from flask import jsonify, session
from .form import signUp
import time


###
# Routing for your application.
###
#WTF_CSRF_ENABLED = False
app.config['SECRET_KEY'] = "javanddukes"

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


@app.route("/timeinfo/")
def timeinfo():
  return time.strftime('%a %d %b %Y')

@app.route('/profile', methods=['GET','POST'])
def profile():
    form=signUp(csrf_enabled=False)
    #import pdb;pdb.set.trace()
    if request.method == 'POST' and form.validate():
      #user=User(request.form['image'],request.form['firstname'],request.form['lastname'] ,request.form['age'], request.form['sex'])
      img=form.image.data 
      #['image']
      #img_func = un + '_' + secure_filename(img.filename) file_path = os.path.join(app.config['UPLOAD_FOLDER'],img_func)
      #img.save(file_path)
      filename = secure_filename(img.filename)
      form.image.data.save(os.path.join('app/static', filename))
      user=SignUp(form.firstname.data, form.lastname.data, form.age.data, form.sex.data,filename)
      db.session.add(user)
      db.session.commit()  
      flash("profile successfully submitted")
    return render_template('signup.html',form=form)
  
@app.route('/profiles',methods=['GET','POST'])
def profiles():
  users=db.session.query(SignUp).all()
  if request.headers['Content-Type']=='application/json':
    lst=[]
    for user in users:
      lst.append({'id':user.id, 'image':user.image, 'fname':user.firstname,'lname':user.lastname,'sex':user.sex, 'age':user.age,'highscore':user.highscore,'tdollar':user.tdollars})
      users={'users':lst}
      return Response(json.dumps(users), mimetype='application/json')
  else:
    return render_template('profiles.html', users=users)
  
@app.route('/profile/<userid>',methods=['GET','POST'])
def profile_view(userid):
  prof=SignUp.query.filter_by(id=userid).first()
  if (request.method == 'POST' or request.headers['Content-Type'] == 'application/json'):
    return jsonify(id=prof.id, firstname=prof.fristname, lastname=prof.lastname, image=prof.image, sex=prof.sex, age=prof.age,highscore=prof.highscore,tdollars=prof.tdollars)
  else:
    user = {'id':prof.id, 'image':prof.image, 'age':prof.age, 'fname':prof.firstname, 'lname':prof.lastname, 'sex':prof.sex,'highscore':prof.highscore,'tdollars':prof.tdollars}
    return render_template('profile.html', user=user,mytime=timeinfo())
  
  

    
if __name__ == '__main__':
  app.run(debug=True,host="0.0.0.0",port="8080")


