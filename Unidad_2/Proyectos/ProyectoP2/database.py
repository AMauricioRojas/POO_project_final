import mysql.connector

def crear_conexion():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",        # Cambia si usas otro usuario
            password="",        # Tu contraseña de MySQL
            database="poo_project_p2"
        )
        return conexion
    except mysql.connector.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
