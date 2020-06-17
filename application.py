from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("hello.html")

@app.route("/hello", methods= ["POST"])
def hello():
    name= request.form.get("name").capitalize()
    country = request.form.get("country") 
    return f"Hello, {name} from {country}"
