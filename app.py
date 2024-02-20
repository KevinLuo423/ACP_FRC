import os

from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask import Flask, render_template
from flask import Flask, render_template, request, flash

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_mail import Mail, Message


app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

app.secret_key = 'secret_developement_key_dont_tell'

class ContactForm(FlaskForm):
  name = StringField("Name",  validators=[DataRequired(message ="Please enter your name.")])
  email = StringField("Email",validators = [DataRequired(message = "Please enter your email address"),Email()])
  subject = StringField("Subject",validators = [DataRequired(message = "Please enter a subject.")])
  message = TextAreaField("Message",validators = [DataRequired(message = "Please enter a message.")])
  submit = SubmitField("Send") 

mail = Mail()
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config['MAIL_USE_SSL'] = True
app.config["MAIL_DEBUG"] = True
app.config["MAIL_USERNAME"] = "srvnp13@gmail.com"
app.config["MAIL_PASSWORD"] = "ujgdkmorybncukqw"
mail.init_app(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html")

@app.route("/FIRST", methods=["GET"])
def FIRST():
    return render_template("FIRST.html")

@app.route("/contact", methods=["GET","POST"])
def contact():
  form = ContactForm()
  if request.method == 'POST':
    if form.validate() == False:
      flash('All fields are required.')
      return render_template('contact.html', form=form)
    else:
      msg = Message(form.subject.data, sender='srvnp13@gmail.com', recipients=['srvnp13@gmail.com'])
      msg.body = """ 
From: %s [%s]  

%s 
""" % (form.name.data, form.email.data, form.message.data)
      mail.send(msg)
      return render_template('contact.html', success=True)
  elif request.method == 'GET':
    return render_template('contact.html', form=form)
 

if __name__ == "__main__":
    app.run(port="5000", debug=True)

