import os
import mysql.connector

from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps



'''
db = mydb = mysql.connector.connect(
    host="todo",
    user="todo",
    passwd="todo",
    database="todo"
)
'''



def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
@login_required
def index():
    #todo
    #main page
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()
    #todo
    
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    #todo
    return render_template("register.html")

@app.route("/cert", methods=["GET", "POST"])
@login_required
def cert():
    #todo
    return render_template("cert.html")

@app.route("/bord", methods=["GET", "POST"])
@login_required
def bord():
    #todo
    return render_template("bord.html")

@app.route("/mypage", methods=["GET", "POST"])
@login_required
def mypage():
    #todo
    return render_template("mypage.html")
