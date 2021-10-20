from flask import Flask, render_template, request, url_for, redirect
from os import getcwd
import pyodbc

# Nombre del controlador.
DRIVER_NAME = "Microsoft Access Driver (*.mdb, *.accdb)"
# Ruta completa del archivo.
DB_PATH = getcwd() + "/Zamna.accdb"
# Establecer la conexión.
conn = pyodbc.connect("Driver={%s};DBQ=%s;" % (DRIVER_NAME, DB_PATH))
# Crear cursor para ejecutar consultas.
cursor = conn.cursor()

domain = "0.0.0.0:8888/"
app = Flask(__name__)


@app.route("/nuser/<user>/<mail>/<passw>")
def nuser(user, mail, passw):

    cursor.execute(u"INSERT INTO Users (Usuario, Correo, Contra) VALUES (?, ?, ?)", user, mail, passw)
    cursor.commit()

    return "DONE"

@app.route("/confirm")
def confirm():
    q = cursor.execute("SELECT Usuario FROM Users")
    rows = q.fetchall()
    if rows is not None:
        for row in rows:
            print(row)
    else:
        print("No hay datos en la tabla.")

    return "DONE"

@app.route("/duser/<user>")
def duser(user):

    cursor.execute(u"DELETE FROM Users VALUES ?", user)
    cursor.commit()

    return "DONE"

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
    app.run(host="0.0.0.0",port="8888",debug=True)