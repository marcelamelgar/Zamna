from flask import Flask, render_template, flash, request, url_for, redirect
from jinja2 import Template, FileSystemLoader, Environment
from requests import get
 
domain = "0.0.0.0:5000/"
templates = FileSystemLoader('templates')
environment = Environment(loader = templates)

app = Flask(__name__)
current_user = "cruz"



@app.route("/", methods=["GET", "POST"]) 
def home():
    global current_user
    peticiones = eval(get(f"http://localhost:8888/peticiones").text)
    categorias = eval(get(f"http://localhost:8888/categorias").text)
    # eval, la funcion de los dioses de python *explosión mental*

    if request.method == "POST":
        id = request.form['id']
        print(id)
        print(id)
        print(id)
        print(id)
        print(id)
        print(id)

    return render_template("home.html", 
            user = current_user, 
            peticiones = peticiones,
            categorias = categorias)

@app.route("/login", methods=["GET", "POST"])
def login():
    error = "" 
    global current_user

    if request.method == "POST":
        user = request.form['username']
        password = request.form['pass']
        print(user, password)

        # Verificación
        response = get(f"http://localhost:8888/confirm/{user}/{password}").text
        print(response)

        if response == "True": 
            current_user = user
            return redirect(url_for('home'))

        error = "El usuario o la contraseña son incorrectas."
    
    return render_template("login.html", error = error)



@app.route("/register", methods=["GET", "POST"])
def register():
    error = "" 
    global current_user

    if request.method == "POST":
        user = request.form['username']
        email = request.form['email']
        password = request.form['pass']
        password2 = request.form['pass2']

        if password == password2: 
            response = get(f"http://localhost:8888/user/nuevo/{user}/{email}/{password}").text

            if response == "True": 
                current_user = user
                print(current_user, "---\n\n'''n\n\n\nn-------------")
                return redirect(url_for('home')) # redirect(url_for('home')

            else: # Si el usuario no existe retorna "False" y se envía el siguiente mensaje 
                error = "Ya existe un usuario con ese nombre"
        
        else:
            error = "Las constraseñas no coinciden"

    return render_template("register.html", error = error)

"""
    if request.method == "POST":
        form = request.form

        # login 
        if form['submit'] == "login": 
            print("LOGIN")

            email = form['email']
            password = form['pass']
            # Si todo está bien dirigir home 
            # guardar usuario activo 
            return redirect("/home")

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
                    return redirect(url_for('home'))

                error = "Ya existe ese usuario, prueba con otro"
                current_user = ""

                # crear el usuario en la base de datos 
"""
    



@app.route("/profile", methods=["GET", "POST"])
def profile():
    # chequear el home de sesión
    # redirigir al perfil 
    # si no se ha iniciado sesión mover a login 

    if current_user != "":
        response = get(f"http://localhost:8888/peticiones/peticion/{id}").text
    else:
        return redirect(url_for('login'))

    return render_template("profile.html")

@app.route("/peticion/<id>", methods=["GET", "POST"])
def peticion(id):
    global current_user
    # chequear el home de sesión
    # redirigir al perfil 
    # si no se ha iniciado sesión mover a login 
    
    if request.method == "POST":
        comment = request.form['comment']
        get(f"http://localhost:8888/comentario/nuevo/{comment}/{current_user}/{id}")
        print(comment)

    response = eval(get(f"http://localhost:8888/peticiones/peticion/{id}").text)
    print(response)

    return render_template("peticion.html", response = response)


@app.route("/<categoria>", methods=["GET", "POST"]) 
def home_cate(categoria):
    global current_user
    peticiones = eval(get(f"http://localhost:8888/peticiones/categoria/{categoria}").text)
    categorias = eval(get(f"http://localhost:8888/categorias").text)
    # eval, la función maestra de pyhton *explosión mental*

    if request.method == "POST":
        id = request.form['id']
        print(id)
        print(id)
        print(id)
        print(id)
        print(id)
        print(id)

    return render_template("home.html",
        user=current_user, 
        peticiones=peticiones, 
        categoria=categoria, 
        categorias = categorias)

@app.route("/rpassword", methods=["GET", "POST"]) 
def reset():
    return render_template("rpassword.html")



if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)