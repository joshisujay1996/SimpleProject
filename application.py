import os
import csv
from flask import Flask, session, redirect, url_for,render_template, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_sqlalchemy  import SQLAlchemy
import requests
import datetime

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


# @app.route("/")
# def index():
    # return "Project 1: TODO"


# link to search the city
@app.route("/data")
def data():

    data = db.execute("SELECT * FROM data").fetchall()
    return render_template("data.html", data=data)



# route to the login and signup
@app.route('/')
def index():
    return render_template('index.html')


# check if the username and password matchs or there is no account
@app.route('/login', methods=["post","GET"])
def login():
    if request.method=="post"
        nm=request.form.get("name")
        pas=request.form.get("password")
        account=db.excute("SELECT * from account").fetchall()
        for accounts in account:
            if ((nm=accounts.name) AND)(pas=accounts.password))
                m=True
            else
                m=False
    return render_template('login.html',value=m)




# signing up and adding values to database
@app.route('/signup', methods = ["POST","GET"])
def signup():
    if request.method == "post":
        name=request.form.get("name")
        password=request.form.get("password")
        db.excute("INSERT INTO account (name,password) VALUES (:a, :b)",
                    {"a": name, "b": password});
        db.commit()
    return render_template('signup.html')


m=[]
# once logged in user will be taken to dashbord
# then user will be checking for the zipcode or the city name to match
@app.route('/dashboard', methods=["POST","GET"])
def dashboard():
    if request.method == "post":
        search=request.form.get("search")
        data1=db.excute("SELECT * from data").fetchall()
        for data in data1:
           m= db.excute("SELECT * FROM data WHERE zipcode like %serch% OR city like %serch% ").fetchclone()
    return render_template('dashboard.html',y=m)


# display the search values
@app.route('/display',method=["POST","GET"])
def display():
    for x in m:
        print(m)


# display the temprature and other values by taking in latitude and longitude values
@app.route('/temp')
def temprature():
    qurey=requests.get("https://api.darksky.net/forecast/0fe0cafa9233688c4149d311cb84b89e/[y.lat],[l.log]").jason()
    temp=query["currently"]["temprature"]
    return(render_template("temp.html",temp=temp))