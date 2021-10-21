from flask import Flask, render_template, request, url_for, redirect
from os import getcwd
import pyodbc

DRIVER_NAME = "Microsoft Access Driver (*.mdb, *.accdb)"
DB_PATH = getcwd() + "/Zamna.accdb"
conn = pyodbc.connect("Driver={%s};DBQ=%s;" % (DRIVER_NAME, DB_PATH))
cursor = conn.cursor()

domain = "0.0.0.0:8888/"
app = Flask(__name__)

#Query para crear un usuario nuevo (VERIFICADO)
@app.route("/user/nuevo/<user>/<mail>/<passw>")
def nuser(user, mail, passw):

    try:
        cursor.execute(u"INSERT INTO Users (Usuario, Correo, Contra) VALUES (?, ?, ?)", user, mail, passw)
        cursor.commit()

        return "True"

    except pyodbc.IntegrityError:
        return "False"


#Query para verificar el inicio de sesion (VERIFICADO)
@app.route("/confirm/<user>/<passw>")
def confirm(user, passw):
    q = cursor.execute("SELECT Usuario FROM Users WHERE Usuario = ?", user)
    usu = q.fetchall()
    q = cursor.execute("SELECT Contra FROM Users WHERE Usuario = ?", user)
    con = q.fetchall()
    
    if usu and con[0][0] == passw:
        return "True"
    
    return "False"


#Query para crear una peticion (VERIFICADO)
@app.route("/peticiones/nuevo/<desc>/<cat>/<fecha>/<crea>")
def npeti(desc, cat, fecha, crea):

    try:
        #Para la fecha, se recibe: dia-mes-ano incluyendo los guiones
        cursor.execute(u"INSERT INTO Peticion (Descripción, Categoria, Fecha, Creador) VALUES (?, ?, ?, ?)", desc, cat, fecha, crea)
        cursor.commit()

        return "True"

    except pyodbc.IntegrityError:
        return "False"


#Query para ver todas las peticiones (VERIFICADO)
@app.route("/peticiones")
def peticiones():
    q = cursor.execute("SELECT * FROM Peticion")
    rows = q.fetchall()
    lista = []

    if rows is not None:
        for row in rows:
            peti = dict(zip(range(len(row)), row))
            lista.append(peti)
    else:
        print("No hay peticiones.")

    sali = dict(zip(range(len(lista)), lista))
    return sali


#Query para ver todas las peticiones de una sola categoria (VERIFICADO)
@app.route("/peticiones/categoria/<cate>")
def pet_esp(cate):
    q = cursor.execute("SELECT * FROM Peticion WHERE Categoria = ?", cate)
    rows = q.fetchall()
    lista = []

    if rows is not None:
        for row in rows:
            peti = dict(zip(range(len(row)), row))
            lista.append(peti)
    else:
        print("No hay peticiones de esa categoria.")

    sali = dict(zip(range(len(lista)), lista))
    return sali


#Query para ver todas las peticiones de una persona (VERIFICADO)
@app.route("/peticiones/creador/<crea>")
def pet_per(crea):
    q = cursor.execute("SELECT * FROM Peticion WHERE Creador = ?", crea)
    rows = q.fetchall()
    lista = []

    if rows is not None:
        for row in rows:
            peti = dict(zip(range(len(row)), row))
            lista.append(peti)
    else:
        print("No hay peticiones para este usuario.")

    sali = dict(zip(range(len(lista)), lista))
    return sali


#Query para ver una peticion y sus comentarios (VERIFICADO)
@app.route("/peticiones/peticion/<id>")
def pet_comen(id):
    q = cursor.execute("SELECT * FROM Peticion WHERE IDPet = ?", id)
    peti = q.fetchall()
    q = cursor.execute("SELECT * FROM Comentarios WHERE IDPeticion = ?", id)
    comen = q.fetchall()
    lista = []

    if peti is not None:
        for row in peti:
            peti = dict(zip(range(len(row)), row))
            lista.append(peti)
        if comen is not None:
            for row2 in comen:
                peti = dict(zip(range(len(row2)), row2))
                lista.append(peti)
        else:
            print("No hay comentarios.")
    else:
        print("No existe esta peticion.")

    sali = dict(zip(range(len(lista)), lista))
    return sali


#Query para borrar una peticion y sus comentarios (VERIFICADO)
@app.route("/peticiones/borrar/<id>")
def dpeti(id):

    cursor.execute(u"DELETE * FROM Peticion WHERE IDPet = ?", id)
    cursor.execute(u"DELETE * FROM Comentarios WHERE IDPeticion = ?", id)
    cursor.commit()

    return "True"


#Query para borrar un comentario (VERIFICADO)
@app.route("/comentario/borrar/<id>")
def dcomen(id):

    cursor.execute(u"DELETE * FROM Comentarios WHERE ID = ?", id)
    cursor.commit()

    return "True"


#Query para crear un comentario (VERIFICADO)
@app.route("/comentario/nuevo/<desc>/<fecha>/<crea>/<id>")
def ncome(desc, fecha, crea, id):

    try:
        #Para la fecha, se recibe: dia-mes-ano incluyendo los guiones
        cursor.execute(u"INSERT INTO Comentarios (Descripcion, Fecha, Creador, IDPeticion) VALUES (?, ?, ?, ?)", desc, fecha, crea, id)
        cursor.commit()

        return "True"

    except pyodbc.IntegrityError:
        return "False"


#Query para ver todos los comentarios de una persona (VERIFICADO)
@app.route("/comentario/creador/<crea>")
def com_per(crea):
    q = cursor.execute("SELECT * FROM Comentarios WHERE Creador = ?", crea)
    rows = q.fetchall()
    lista = []

    if rows is not None:
        for row in rows:
            peti = dict(zip(range(len(row)), row))
            lista.append(peti)
    else:
        print("No hay comentarios para este usuario.")

    sali = dict(zip(range(len(lista)), lista))
    return sali


#Query para ver todas las categorias (VERIFICADO)
@app.route("/categorias")
def categorias():
    q = cursor.execute("SELECT Categoria FROM Peticion")
    rows = q.fetchall()
    lista = []

    if rows is not None:
        for row in rows:
            peti = dict(zip(range(len(row)), row))
            lista.append(peti)
    else:
        print("No hay categorias.")

    sali = dict(zip(range(len(lista)), lista))
    return sali


#Query para borrar un usuario (VERIFICADO)
@app.route("/user/borrar/<user>")
def duser(user):

    cursor.execute(u"DELETE * FROM Users WHERE Usuario = ?", user)
    cursor.execute(u"DELETE * FROM Peticion WHERE Creador = ?", user)
    cursor.execute(u"DELETE * FROM Comentarios WHERE Creador = ?", user)
    cursor.commit()

    return "True"


#Query para apagar el servidor (VERIFICADO)
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