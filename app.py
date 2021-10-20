from flask import Flask, render_template, flash, request, url_for, redirect
from jinja2 import Template, FileSystemLoader, Environment

domain = "0.0.0.0:5000/"
templates = FileSystemLoader('templates')
environment = Environment(loader = templates)

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

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

        # register
        if form['submit'] == "register":
            print("REGISTRO")
            email = form['regemail']
            password = form['regpass']
            rpassword = form['reregpass']
            # Verificar que el usuario sea nuevo
            
            if password and password != rpassword:
                print(password, rpassword)
                error = 'Las contraseñas no coinciden'
                return render_template("login.html", error = error)
            else: 
                current_user = email # guarda el usuario activo 

                # crear el usuario en la base de datos 
                return redirect(url_for('inicio'))
                
                       
        
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

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)