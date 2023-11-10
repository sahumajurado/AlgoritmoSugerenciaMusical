import mysql.connector as mysql

def establecer_conexion():
    try:
        conexion = mysql.connect(
            user='root',
            password="12345678",
            host="localhost",
            database="db_reproductormusical",
            port="3306"
        )
        print("Conexión exitosa:", conexion)
        return conexion

    except mysql.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None


def cerrar_conexion(conexion):
    if conexion and conexion.is_connected():
       conexion.close()

