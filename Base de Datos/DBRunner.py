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

        return "True"

    except pyodbc.IntegrityError:
        return "False"

#Query para ver todas las peticiones
@app.route("/peticiones")
def peticiones():
    q = cursor.execute("SELECT * FROM Peticion")
    rows = q.fetchall()
    if rows is not None:
        for row in rows:
            print(row)
    else:
        print("No hay datos en la tabla.")

    return "Debo cambiarlo a Tupla o Dicci"

#Query para ver todas las peticiones de una sola categoria
@app.route("/peticiones/categoria/<cate>")
def pet_esp(cate):
    q = cursor.execute("SELECT * FROM Peticion WHERE Categoria = ?", cate)
    rows = q.fetchall()
    if rows is not None:
        for row in rows:
            print(row)
    else:
        print("No hay datos en la tabla.")

    return "Debo cambiarlo a Tupla o Dicci"

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