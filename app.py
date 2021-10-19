from flask import Flask, render_template, request, url_for, redirect
from jinja2 import Template, FileSystemLoader, Environment

domain = "0.0.0.0:5000/"
templates = FileSystemLoader('templates')
environment = Environment(loader = templates)

app = Flask(__name__)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # login 
        form = request.form
        print(form)
        email = request.form['email']
        password = request.form['pass']
        print(email, password)

        # register 


        # if all is well go to inicio
    return render_template("login.html")

@app.route("/", methods=["GET", "POST"])
def inicio():
    # chequear el inicio de sesión 
    return render_template("login.html")


@app.route("/perfil", methods=["GET", "POST"])
def pefil():
    # chequear el inicio de sesión
    # redirigir al perfil 
    # si no se ha iniciado sesión mover a login 
    return render_template("login.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)