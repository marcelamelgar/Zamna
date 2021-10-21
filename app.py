from flask import Flask, render_template, flash, request, url_for, redirect
from jinja2 import Template, FileSystemLoader, Environment
from requests import get
 
domain = "0.0.0.0:5000/"
templates = FileSystemLoader('templates')
environment = Environment(loader = templates)

app = Flask(__name__)

current_user = ""

@app.route("/", methods=["GET", "POST"]) 
def inicio():
    global current_user
    if current_user:
        print(current_user)
    # chequear el inicio de sesión 
    # hacer solicitud de todas las peticiones 
    return render_template("inicio.html", user = current_user)

@app.route("/login", methods=["GET", "POST"])
def login():
    error = "" 
    global current_user

    if request.method == "POST":
        form = request.form

        # login 
        if form['submit'] == "login": 
            print("LOGIN")

            email = form['email']
            password = form['pass']
            # Si todo está bien dirigir inicio 
            # guardar usuario activo 
            return redirect(url_for('inicio'))

        # register
        if form['submit'] == "register":
            print("REGISTRO")
            user = "daniel"
            email = form['regemail']
            password = form['regpass']
            rpassword = form['reregpass']
            # Verificar que el usuario sea nuevo
            
            if password and password != rpassword:
                print(password, rpassword)
                error = 'Las contraseñas no coinciden'

            else: 
                response = get(f"localhost:8888/nuser/{user}/{email}/{password}")
                if response == "True":
                    current_user = user # guarda el usuario activo 
                    return redirect(url_for('inicio'))

                error = "Ya existe ese usuario, prueba con otro"
                current_user = ""

                # crear el usuario en la base de datos 
        
    return render_template("login.html", error = error)


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

@app.route("/rpassword", methods=["GET", "POST"]) 
def reset():
    return render_template("rpassword.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)