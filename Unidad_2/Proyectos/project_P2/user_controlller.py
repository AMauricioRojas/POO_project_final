# Controlador para operaciones CRUD sobre la tabla usuarios
from database import crear_conexion

def obtener_usuarios():
    conexion = crear_conexion()
    if not conexion:
        return []
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT id, usuario, password FROM usuarios ORDER BY id")
        rows = cursor.fetchall()
        cursor.close()
        conexion.close()
        return rows
    except Exception as e:
        print("Error al obtener usuarios:", e)
        return []

def agregar_usuario(usuario, password):
    if not usuario or not password:
        return False, "Campos vacíos"
    conexion = crear_conexion()
    if not conexion:
        return False, "Error de conexión"
    try:
        cursor = conexion.cursor()
        consulta = "INSERT INTO usuarios (usuario, password) VALUES (%s, %s)"
        cursor.execute(consulta, (usuario, password))
        conexion.commit()
        cursor.close()
        conexion.close()
        return True, "Usuario agregado correctamente"
    except Exception as e:
        print("Error al agregar usuario:", e)
        return False, str(e)

def actualizar_usuario(user_id, usuario, password):
    if not usuario or not password:
        return False, "Campos vacíos"
    conexion = crear_conexion()
    if not conexion:
        return False, "Error de conexión"
    try:
        cursor = conexion.cursor()
        consulta = "UPDATE usuarios SET usuario = %s, password = %s WHERE id = %s"
        cursor.execute(consulta, (usuario, password, user_id))
        conexion.commit()
        affected = cursor.rowcount
        cursor.close()
        conexion.close()
        if affected == 0:
            return False, "No se encontró el usuario"
        return True, "Usuario actualizado correctamente"
    except Exception as e:
        print("Error al actualizar usuario:", e)
        return False, str(e)

def eliminar_usuario(user_id):
    conexion = crear_conexion()
    if not conexion:
        return False, "Error de conexión"
    try:
        cursor = conexion.cursor()
        consulta = "DELETE FROM usuarios WHERE id = %s"
        cursor.execute(consulta, (user_id,))
        conexion.commit()
        affected = cursor.rowcount
        cursor.close()
        conexion.close()
        if affected == 0:
            return False, "No se encontró el usuario"
        return True, "Usuario eliminado correctamente"
    except Exception as e:
        print("Error al eliminar usuario:", e)
        return False, str(e)
