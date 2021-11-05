from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, Form, BooleanField,  PasswordField, validators
from wtforms.validators import DataRequired






app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/login')
def login():
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    return render_template("login.html")



if __name__ == "__main__":
    app.run(debug=True)
