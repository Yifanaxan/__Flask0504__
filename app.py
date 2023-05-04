from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.jinja.html")


@app.route("/")
def learning():
    return render_template("learning.jinja.html")

