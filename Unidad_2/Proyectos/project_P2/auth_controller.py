# Controlador de autenticación
from database import crear_conexion

def validar_credenciales(usuario, password):
    conexion = crear_conexion()
    if not conexion:
        return False

    try:
        cursor = conexion.cursor()
        consulta = "SELECT id FROM usuarios WHERE usuario = %s AND password = %s"
        cursor.execute(consulta, (usuario, password))
        result = cursor.fetchone()
        cursor.close()
        conexion.close()
        return bool(result)
    except Exception as e:
        print("Error al validar credenciales:", e)
        return False
