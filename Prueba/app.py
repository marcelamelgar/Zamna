from flask import Flask, render_template, request, url_for, redirect
from jinja2 import Template, FileSystemLoader, Environment

domain = "0.0.0.0:5000/"
templates = FileSystemLoader('templates')
environment = Environment(loader = templates)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"]) 
def inicio():
    # chequear el inicio de sesión 
    # hacer solicitud de todas las peticiones 
    return render_template("login.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        form = request.form

        # for i in form: 
        #     print("  ",i, ":", form[i])
        
        # login 
        if form['submit'] == "login": 
            print("LOGIN")

            email = form['email']
            password = form['pass']
            # Si todo está bien dirigir inicio 
            # guardar usuario activo 


        # register
        if form['submit'] == "register":
            print("REGISTRO") 

            # Verificar que el usuario sea nuevo 
            email = form['regemail']
            password = form['regpass']
            rpassword = form['reregpass']
            # Si todo está bien dirigir inicio         
            # guardar usuario activo 
        
    return render_template("login.html")


@app.route("/perfil", methods=["GET", "POST"])
def pefil():
    # chequear el inicio de sesión
    # redirigir al perfil 
    # si no se ha iniciado sesión mover a login 
    return render_template("login.html")


@app.route("/<categoria>", methods=["GET", "POST"]) 
def inicio_cate(categoria):
    print(categoria)
    # chequear el inicio de sesión
    # Hacer solcitud de las petiones 
    return render_template("login.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)