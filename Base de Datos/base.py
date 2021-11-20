from os import getcwd
import pyodbc
import datetime
from requests import get


DRIVER_NAME = "Microsoft Access Driver (*.mdb, *.accdb)"
DB_PATH = getcwd() + "/Pruebas.accdb"
conn = pyodbc.connect("Driver={%s};DBQ=%s;" % (DRIVER_NAME, DB_PATH))
cursor = conn.cursor()

#Query para crear un usuario nuevo (VERIFICADO)
def nuser(user, mail, passw):

    try:
        cursor.execute(u"INSERT INTO Users (Usuario, Correo, Contra) VALUES (?, ?, ?)", user, mail, passw)
        cursor.commit()

        return "True"

    except pyodbc.IntegrityError:
        return "False"


#Query para verificar el inicio de sesion (VERIFICADO)
def confirm(user, passw):
    q = cursor.execute("SELECT Usuario FROM Users WHERE Usuario = ?", user)
    usu = q.fetchall()
    q = cursor.execute("SELECT Contra FROM Users WHERE Usuario = ?", user)
    con = q.fetchall()
    
    if usu and con[0][0] == passw:
        return "True"
    
    else:
        return "False"

#Query para ver la informacion de una persona
def infoUser(user):
    q = cursor.execute("SELECT * FROM Users WHERE Usuario = ?", user)
    rows = q.fetchall()
    lista = []

    if rows is not None:
        for row in rows:
            peti = dict(zip(range(len(row)), row))
            lista.append(peti)
    else:
        return "No hay datos del usuario."

    sali = dict(zip(range(len(lista)), lista))
    return sali

#Query para crear una peticion (VERIFICADO)
def npeti(desc, cat, crea):
    fecha = "22-10-2021"

    try:
        #Para la fecha, se recibe: dia-mes-ano incluyendo los guiones
        cursor.execute(u"INSERT INTO Peticion (Descripción, Categoria, Fecha, Creador) VALUES (?, ?, ?, ?)", desc, cat, fecha, crea)
        cursor.commit()

        return "True"

    except pyodbc.IntegrityError:
        return "False"


#Query para ver todas las peticiones (VERIFICADO)
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
def dpeti(id):

    cursor.execute(u"DELETE * FROM Peticion WHERE IDPet = ?", id)
    cursor.execute(u"DELETE * FROM Comentarios WHERE IDPeticion = ?", id)
    cursor.commit()

    return "True"


#Query para borrar un comentario (VERIFICADO)
def dcomen(id):

    cursor.execute(u"DELETE * FROM Comentarios WHERE ID = ?", id)
    cursor.commit()

    return "True"


#Query para crear un comentario (VERIFICADO)
def ncome(desc, crea, id):
    fecha = "22-10-2021"

    try:
        #Para la fecha, se recibe: dia-mes-ano incluyendo los guiones
        cursor.execute(u"INSERT INTO Comentarios (Descripcion, Fecha, Creador, IDPeticion) VALUES (?, ?, ?, ?)", desc, fecha, crea, id)
        cursor.commit()

        return "True"

    except pyodbc.IntegrityError:
        return "False"


#Query para ver todos los comentarios de una persona (VERIFICADO)
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
def duser(user):

    peticiones = pet_per(user)

    for i in range(len(peticiones)):
        cursor.execute(u"DELETE * FROM Peticion WHERE IDPet = ?", int(peticiones[i][0]))
        cursor.execute(u"DELETE * FROM Comentarios WHERE IDPeticion = ?", int(peticiones[i][0]))

    cursor.execute(u"DELETE * FROM Users WHERE Usuario = ?", user)
    cursor.execute(u"DELETE * FROM Peticion WHERE Creador = ?", user)
    cursor.execute(u"DELETE * FROM Comentarios WHERE Creador = ?", user)

    cursor.commit()

    return "True"
