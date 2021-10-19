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

usu = "danbehar"
cor = "danielbehar@ufm.edu"
con = "4515RNya"

# Ejecutar la consulta.
cursor.execute(u"INSERT INTO Users (Usuario, Correo, Contra) VALUES (?, ?, ?)", usu, cor, con)

# Guardar los cambios.
cursor.commit()
# Ejecutar consulta: retornar todas las filas de la tabla empleados.
#q = cursor.execute("SELECT * FROM Users")
#q = cursor.execute("SELECT Usuario FROM Users WHERE id = 1")
q = cursor.execute("SELECT Usuario FROM Users")
rows = q.fetchall()
# Recorrer cada una de las filas e imprimirlas en pantalla.
if rows is not None:
    for row in rows:
        print(row)
else:
    print("No hay datos en la tabla.")
# Cerrar la conexión y, opcionalmente, el cursor antes de finalizar.
cursor.close()
conn.close()