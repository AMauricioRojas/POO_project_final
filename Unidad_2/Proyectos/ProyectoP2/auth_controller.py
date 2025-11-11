#Controlador encargado de la logica de autentificacion,nos sirve para separar la logica de logi para mantener el codigo limpio
from database import crear_conexion

def validar_credenciales(username, password):
    conexion = crear_conexion()
    if not conexion:
        return False
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE username = %s AND password = %s", (username, password))
        resultado = cursor.fetchone()
        conexion.close()
        return resultado is not None
    except Exception as e:
        print(f"Error al validar credenciales: {e}")
        return False
