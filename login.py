import Conexion
import sys
import pygame
import getpass
# Crear un cursor
conexion = Conexion.establecer_conexion()
cursor = conexion.cursor()

print("---------------------------------------")
print("Bienvenido al reproductor musical PyArd")
print("---------------------------------------")

def menu_principal():
    print("Seleccione alguna de las siguientes opciones: ")
    print("1. Ingresar cuenta existente")
    print("2. Registrarse")
    print("3. Salir de la aplicación")

def registrar_usuario():
    nombre = input("Ingresar nombre: ")
    apellido = input("Ingresar apellidos: ")
    sexo = input("Ingrese su género: ")
    fecha_nacimiento = input("Ingresar fecha de nacimiento (Año-mes-día): ")
    nacionalidad = input("Ingresar nacionalidad: ")
    correo = input("Ingresar correo electrónico: ")
    nombre_user = input("Cree su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    # Consulta parametrizada para la inserción de datos
    query = "INSERT INTO usuario(nombre, apellido, sexo, fecha_nacimiento, nacionalidad, correo, nombre_user, contraseña) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    datos_usuario = (nombre, apellido, sexo, fecha_nacimiento, nacionalidad, correo, nombre_user, contraseña)

    try:
        cursor.execute(query, datos_usuario)
        conexion.commit()
        print("---------------------------------------")
        print("Usuario registrado con éxito.")
    except Exception as e:
        print("---------------------------------------")
        print(f"Error al registrar usuario: {e}")

def login():
    user = input("Ingrese su usuario: ")
    password = getpass.getpass("Ingrese su contraseña: ")

    # Consulta parametrizada para verificar las credenciales
    query_usuario = "SELECT * FROM usuario WHERE nombre_user = %s AND contraseña = %s"
    datos_usuario = (user, password)

    try:
        cursor.execute(query_usuario, datos_usuario)
        resultado_usuario = cursor.fetchone()

        if resultado_usuario:
            print("---------------------------------------")
            print("Inicio de sesión exitoso.")
            print("---------------------------------------")
        else:
            print("---------------------------------------")
            print("Credenciales incorrectas. Intente nuevamente.")
            print("---------------------------------------")
    except Exception as e:
        print(f"Error al ingresar: {e}")

def salir():
    cursor.close()
    Conexion.cerrar_conexion(conexion)
    sys.exit()

def listar_canciones():
    query_canciones = """
    SELECT c.id_cancion, c.nombre AS nombre_cancion, a.nombre AS nombre_artista, al.nombre AS nombre_album, g.nombre AS nombre_genero
    FROM cancion AS c
    JOIN artista AS a ON c.id_artista = a.id_artista
    JOIN album AS al ON c.id_album = al.id_album
    JOIN generomusical AS g ON c.id_generomusical = g.id_generomusical;
    """
    cursor.execute(query_canciones)
    resultado_cancion = cursor.fetchone()
    while resultado_cancion:
        print(resultado_cancion)
        resultado_cancion = cursor.fetchone()

def reproducir_musica():
    cancion_id = input("Seleccione la canción a escuchar (ingrese el ID): ")
    query_listar = "SELECT * FROM cancion WHERE id_cancion = %s"
    datos_cancion = (cancion_id,)

    try:
        cursor.execute(query_listar, datos_cancion)
        cancion = cursor.fetchone()

        if cancion:
            # Ajusta la consulta según tus necesidades
            query_reproducir = "SELECT archivo_musica FROM cancion WHERE id_cancion = %s"
            datos_reproducir = (cancion_id,)
            cursor.execute(query_reproducir, datos_reproducir)
            archivo_musica = cursor.fetchone()[0]

            pygame.mixer.init()
            pygame.mixer.music.load(archivo_musica)
            pygame.mixer.music.play()

            while True:
                opcion = input("Seleccione una opción:\n1. Pausar\n2. Continuar\n3. Detener\n")

                if opcion == "1":
                    pygame.mixer.music.pause()
                elif opcion == "2":
                    pygame.mixer.music.unpause()
                elif opcion == "3":
                    pygame.mixer.music.stop()
                    break
                else:
                    print("Opción no válida. Intente nuevamente.")
        else:
            print("Canción no encontrada.")
    except Exception as e:
        print(f"Error al reproducir música: {e}")

# Menú principal
while True:
    menu_principal()
    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == "1":
        login()
        listar_canciones()
        reproducir_musica()
    elif opcion == "2":
        registrar_usuario()
    elif opcion == "3":
        salir()
    else:
        print("Opción no válida. Intente nuevamente.")