import mysql.connector
from mysql.connector import Error

def crear_conexion():
    """Crea y devuelve una conexión a la base de datos MySQL.
    Ajusta los parámetros si tu servidor usa otro usuario/contraseña/host."""
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='POO_project_P2'
        )
        if conexion.is_connected():
            return conexion
    except Error as e:
        print("Error de conexión a la base de datos:", e)
        return None
