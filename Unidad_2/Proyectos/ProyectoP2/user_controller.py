from database import crear_conexion

# CREATE
def agregar_usuario(username, password):
    conexion = crear_conexion()
    if not conexion:
        return False
    try:
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO usuarios (username, password) VALUES (%s, %s)", (username, password))
        conexion.commit()
        conexion.close()
        return True
    except Exception as e:
        print(f"Error al agregar usuario: {e}")
        conexion.close()
        return False

# READ
def ver_usuarios():
    conexion = crear_conexion()
    if not conexion:
        return []
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT ID, username, password FROM usuarios")
        resultado = cursor.fetchall()
        conexion.close()
        return resultado
    except Exception as e:
        print(f"Error al obtener usuarios: {e}")
        conexion.close()
        return []

# UPDATE
def actualizar_usuario(user_id, nuevo_username, nueva_password):
    conexion = crear_conexion()
    if not conexion:
        return False
    try:
        cursor = conexion.cursor()
        cursor.execute("UPDATE usuarios SET username = %s, password = %s WHERE ID = %s",
                       (nuevo_username, nueva_password, user_id))
        conexion.commit()
        conexion.close()
        return True
    except Exception as e:
        print(f"Error al actualizar usuario: {e}")
        conexion.close()
        return False

# DELETE
def eliminar_usuario(user_id):
    conexion = crear_conexion()
    if not conexion:
        return False
    try:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM usuarios WHERE ID = %s", (user_id,))
        conexion.commit()
        conexion.close()
        return True
    except Exception as e:
        print(f"Error al eliminar usuario: {e}")
        conexion.close()
        return False
