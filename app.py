from flask import Flask, render_template, flash, request, url_for, redirect
from jinja2 import Template, FileSystemLoader, Environment
from requests import get
import datetime
from database.base import nuser, confirm, infoUser, npeti, peticiones, pet_esp, pet_per, pet_comen, dpeti, dcomen, ncome, com_per, categorias, duser
 
domain = "0.0.0.0:5000/"
templates = FileSystemLoader('templates')
environment = Environment(loader = templates)

app = Flask(__name__)
current_user = ""

@app.route("/", methods=["GET", "POST"]) 
def home():
    global current_user
    petitions = peticiones()
    petitions = eval(petitions)
    categories = categorias()
    categories = eval(categories)

    if request.method == "POST":
        id = request.form['id']

    return render_template("home.html", 
            user = current_user, 
            petitions = petitions,
            categorias = categories)

@app.route("/login", methods=["GET", "POST"])
def login():
    error = "" 
    global current_user

    if request.method == "POST":
        user = request.form['username']
        password = request.form['pass']

        # Verificación
        response = confirm(user, password)

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
        npeti(comment, categ, current_user)
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
            response = nuser(user, email, password)            

            if response == "True": 
                current_user = user
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
            dpeti(id)           

        if delete[0] == 'c':
            id = int(delete[1:])
            dcomen(id)
            
        if delete[0] == 'u':
            user = delete[1:]
            duser(user)
            current_user = ""

    if current_user != "":
        pet_perso = eval(pet_per(current_user))
        com_perso = eval(com_per(current_user))
        info = eval(infoUser(current_user))
    else:
        return redirect(url_for('login'))

    return render_template("profile.html", info = info, pet_perso = pet_perso, com_perso = com_perso)

@app.route("/peticion/<id>", methods=["GET", "POST"])
def peticion(id):
    global current_user
    
    if request.method == "POST":
        comment = request.form['comment']
        ncome(comment, current_user, id)

    response = eval(pet_comen(id))

    return render_template("peticion.html", response = response)


@app.route("/<categoria>", methods=["GET", "POST"]) 
def home_cate(categoria):
    global current_user
    petitions = eval(pet_esp(categoria))
    categories = eval(categorias())

    if request.method == "POST":
        id = request.form['id']

    return render_template("home.html",
        user=current_user, 
        petitions=petitions, 
        categoria=categoria, 
        categorias = categories)

@app.route("/rpassword", methods=["GET", "POST"]) 
def reset():
    return render_template("rpassword.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)