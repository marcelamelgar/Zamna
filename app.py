from flask import Flask, render_template, request, url_for, redirect
from jinja2 import Template, FileSystemLoader, Environment

domain = "0.0.0.0:5000/"
templates = FileSystemLoader('templates')
environment = Environment(loader = templates)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        form = request.form
        print(form)
        email = request.form['email']
        password = request.form['pass']
        print(email, password)
    return render_template("login.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)