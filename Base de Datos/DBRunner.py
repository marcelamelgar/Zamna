from flask import Flask, render_template, request, url_for, redirect
from os import getcwd
import pyodbc

DRIVER_NAME = "Microsoft Access Driver (*.mdb, *.accdb)"
DB_PATH = getcwd() + "/Zamna.accdb"
conn = pyodbc.connect("Driver={%s};DBQ=%s;" % (DRIVER_NAME, DB_PATH))
cursor = conn.cursor()

domain = "0.0.0.0:8888/"
app = Flask(__name__)

#Query para crear un usuario nuevo
@app.route("/user/nuevo/<user>/<mail>/<passw>")
def nuser(user, mail, passw):

    try:
        cursor.execute(u"INSERT INTO Users (Usuario, Correo, Contra) VALUES (?, ?, ?)", user, mail, passw)
        cursor.commit()

        return "True"

    except pyodbc.IntegrityError:
        return "False"


#Query para verificar el inicio de sesion
@app.route("/confirm/<user>/<passw>")
def confirm(user, passw):
    q = cursor.execute("SELECT Usuario FROM Users WHERE Usuario = ?", user)
    usu = q.fetchall()
    q = cursor.execute("SELECT Contra FROM Users WHERE Usuario = ?", user)
    con = q.fetchall()
    
    if usu and con[0][0] == passw:
        return "True"
    else:
        return "False"


#Query para crear una peticion
@app.route("/peticiones/nueva/<desc>/<cat>/<fecha>/<crea>")
def npeti(desc, cat, fecha, crea):

    try:
        #Para la fecha, se recibe: dia-mes-ano incluyendo los guiones
        cursor.execute(u"INSERT INTO Peticion (Descripción, Categoria, Fecha, Creador) VALUES (?, ?, ?, ?)", desc, cat, fecha, crea)
        cursor.commit()

        return "Creado"

    except pyodbc.IntegrityError:
        return "No Creado"


#Query para ver todas las peticiones
@app.route("/peticiones")
def peticiones():
    q = cursor.execute("SELECT * FROM Peticion")
    rows = q.fetchall()

    if rows is not None:
        for row in rows:
            print(row)
    else:
        print("No hay peticiones.")

    return "Todas las peticiones debo cambiarlo a Tupla o Dicci"


#Query para ver todas las peticiones de una sola categoria
@app.route("/peticiones/categoria/<cate>")
def pet_esp(cate):
    q = cursor.execute("SELECT * FROM Peticion WHERE Categoria = ?", cate)
    rows = q.fetchall()

    if rows is not None:
        for row in rows:
            print(row)
    else:
        print("No hay peticiones de esa categoria.")

    return "Peticiones por cat debo cambiarlo a Tupla o Dicci"


#Query para ver todas las peticiones de una persona
@app.route("/peticiones/creador/<crea>")
def pet_per(crea):
    q = cursor.execute("SELECT * FROM Peticion WHERE Creador = ?", crea)
    rows = q.fetchall()

    if rows is not None:
        for row in rows:
            print(row)
    else:
        print("No hay peticiones para este usuario.")

    return "Peticiones por usuario debo cambiarlo a Tupla o Dicci"


#Query para ver una peticion y sus comentarios
@app.route("/peticiones/peticion/<id>")
def pet_comen(id):
    q = cursor.execute("SELECT * FROM Peticion WHERE IDPet = ?", id)
    peti = q.fetchall()
    q = cursor.execute("SELECT * FROM Comentarios WHERE IDPeticion = ?", id)
    comen = q.fetchall()

    if peti is not None:
        for row in peti:
            print(row)
        if comen is not None:
            for row2 in comen:
                print(row2)
        else:
            print("No hay comentarios.")
    else:
        print("No existe esta peticion.")

    return "Peticion y comentarios debo cambiarlo a Tupla o Dicci"


#Query para borrar una peticion y sus comentarios
@app.route("/peticiones/borrar/<id>")
def dpeti(id):

    cursor.execute(u"DELETE * FROM Peticion WHERE IDPet = ?", id)
    cursor.execute(u"DELETE * FROM Comentarios WHERE IDPeticion = ?", id)
    cursor.commit()

    return "DONE"


#Query para borrar un comentario
@app.route("/comentarios/borrar/<id>")
def dcomen(id):

    cursor.execute(u"DELETE * FROM Comentarios WHERE ID = ?", id)
    cursor.commit()

    return "DONE"


#Query para crear un comentario
@app.route("/comentario/nueva/<desc>/<fecha>/<crea>/<id>")
def ncome(desc, fecha, crea, id):

    try:
        #Para la fecha, se recibe: dia-mes-ano incluyendo los guiones
        cursor.execute(u"INSERT INTO Comentarios (Descripción, Fecha, Creador, IDPeticion) VALUES (?, ?, ?, ?)", desc, fecha, crea, id)
        cursor.commit()

        return "Creado"

    except pyodbc.IntegrityError:
        return "No Creado"


#Query para ver todos los comentarios de una persona
@app.route("/comentarios/creador/<crea>")
def com_per(crea):
    q = cursor.execute("SELECT * FROM Comentarios WHERE Creador = ?", crea)
    rows = q.fetchall()
    if rows is not None:
        for row in rows:
            print(row)
    else:
        print("No hay comentarios para este usuario.")

    return "Comentarios por usu debo cambiarlo a Tupla o Dicci"


#Query para ver todas las categorias
@app.route("/categorias")
def categorias():
    q = cursor.execute("SELECT Categoria FROM Peticion")
    rows = q.fetchall()

    if rows is not None:
        for row in rows:
            print(row)
    else:
        print("No hay categorias.")

    return "Todas las categorias debo cambiarlo a Tupla o Dicci"


#Query para borrar un usuario
@app.route("/user/borrar/<user>")
def duser(user):

    cursor.execute(u"DELETE * FROM Users WHERE Usuario = ?", user)
    cursor.execute(u"DELETE * FROM Peticion WHERE Creador = ?", user)
    cursor.execute(u"DELETE * FROM Comentarios WHERE Creador = ?", user)
    cursor.commit()

    return "DONE"


#Query para apagar el servidor
def shutdown_server():
    cursor.close()
    conn.close()
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    
@app.route('/shutdown', methods=['GET'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8888", debug=True)