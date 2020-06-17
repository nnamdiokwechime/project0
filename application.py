from flask import Flask, render_template, request, session
from flask_session import Session
app = Flask(__name__)

app.config["SESSION_PERMANENT"]= False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    return render_template("hello.html")

@app.route("/hello", methods= ["POST"])
def hello():
    session["name"]= request.form.get("name").capitalize()
    session["country"] = request.form.get("country")
    return f"Hello, {session['name']} from {session['country']}"
