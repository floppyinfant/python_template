#!/usr/bin/env python

"""
file ./routes.py

# Code from @see Learning Flask, PacktLib
"""

# -----------------------------------------

from flask import Flask, render_template, request, session, redirect, url_for
# import os
from examples.flask.htdocs.models import db, User
from examples.flask.htdocs.forms import SignupForm

# -----------------------------------------

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/learningflask'
db.init_app(app)

app.secret_key = "development-key"

# -----------------------------------------

@app.route("/")
def index():
     return render_template("index.html")

@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/goodbye/<name>")
def goodbye(name):
     return "Goodbye %s!" % name

@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignupForm()

    if request.method == "POST":
        if form.validate() == False:
            return render_template('signup.html', form=form)
        else:
            newuser = User(form.first_name.data, form.last_name.data, form.email.data, form.password.data)
            db.session.add(newuser)
            db.session.commit()
            return 'Success!'

    elif request.method == "GET":
        return render_template('signup.html', form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if request.method == "POST":
        if form.validate() == False:
            return render_template("login.html", form=form)
        else:
            email = form.email.data
            password = form.password.data
            user = User.query.filter_by(email=email).first()
            if user is not None and user.check_password(password):
                session['email'] = form.email.data
                return redirect(url_for('home'))
            else:
                return redirect(url_for('login'))

    elif request.method == 'GET':
        return render_template('login.html', form=form)

@app.route("/logout")
def logout():
    session.pop('email', None)
    return redirect(url_for('index'))

@app.route("/home", methods=["GET", "POST"])
def home():
    return render_template("home.html")

# -----------------------------------------

if __name__ == '__main__':
      # port = int(os.environ.get('PORT', 5000))
      # app.run(host='127.0.0.1', port=port, debug=True)
     app.run(debug=True)
