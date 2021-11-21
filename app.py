from flask import Flask, render_template, flash, request, url_for, redirect
from jinja2 import Template, FileSystemLoader, Environment
from requests import get
import database.base as db 
 
domain = "0.0.0.0:5000/"
templates = FileSystemLoader('templates')
environment = Environment(loader = templates)

app = Flask(__name__)
current_user = ""

print(db.confirm("daniel", "1234mayuscula")) #Prueba de que la base de datos está funcionando como función :) felicidad! 

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

@app.route("/nueva_peticion", methods=["GET", "POST"])
def nueva_peticion():
    global current_user

    if request.method == "POST":
        categ = request.form['categ']
        comment = request.form['comment']
        get(f"http://localhost:8888/peticiones/nuevo/{comment}/{categ}/{current_user}")
        return redirect(url_for('home'))

    return render_template("ask.html")

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
    

@app.route("/profile", methods=["GET", "POST"])
def profile():
    global current_user
    
    if request.method == "POST":
        delete = request.form['delete']

        if delete[0] == 'p':
            id = int(delete[1:])
            print(id)
            get(f"http://localhost:8888/peticiones/borrar/{id}")            

        if delete[0] == 'c':
            id = int(delete[1:])
            print(id)
            get(f"http://localhost:8888/comentario/borrar/{id}")
            
        if delete[0] == 'u':
            user = delete[1:]
            print(user)
            get(f"http://localhost:8888/user/borrar/{user}")
            current_user = ""

    if current_user != "":
        pet_perso = eval(get(f"http://localhost:8888/peticiones/creador/{current_user}").text)
        com_perso = eval(get(f"http://localhost:8888/comentario/creador/{current_user}").text)
        info = eval(get(f"http://localhost:8888/user/datos/{current_user}").text)
    else:
        return redirect(url_for('login'))

    return render_template("profile.html", info = info, pet_perso = pet_perso, com_perso = com_perso)

@app.route("/peticion/<id>", methods=["GET", "POST"])
def peticion(id):
    global current_user
    
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