from flask import Flask, render_template, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField

app = Flask(__name__)
app.secret_key = "giantpotato"

ACCESS_CODE = "42"

users = {}

class User:
    def __init__(self, realname, username, password):
        self.realname = realname
        self.username = username
        self.password = password
class loginform(FlaskForm):
    username = StringField("username")
    password = PasswordField("password")
    submit = SubmitField("log in")
class RegisterForm(FlaskForm):
    realname = StringField("realname")
    username = StringField("username")
    password = PasswordField("password")
    password2 = PasswordField("password2")
    accesscode = PasswordField("accesscode")
    submit = SubmitField("register")
@app.route("/register", methods=["GET","POST"])
def register():
    form = RegisterForm()
    if form.is_submitted():
        realname = form.realname.data
        username = form.username.data
        password = form.password.data
        password2 = form.password2.data
        accesscode = form.accesscode.data
        if accesscode == ACCESS_CODE and password == password2:
            print("Access code correct, regestering user.")
            new_user = User(realname, username, password)
            users[username] = new_user
            return redirect(url_for("login"))
        else:
            print(accesscode)
            print(ACCESS_CODE)
            print(password)
            print(password2)
            print("access code incorrect or passwords do not match")
            return render_template("register.html", form=form)
    else:
        return render_template("register.html", form=form)
@app.route("/login", methods=["GET","POST"])
def login():
    form = loginform()
    if form.is_submitted():
        pass
    else:
        print("Access code incorect")
        return render_template("login.html", form=form)