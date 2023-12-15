import Conexion
import sys
import pygame
import webbrowser

# Crear un cursor
conexion = Conexion.establecer_conexion()
cursor = conexion.cursor()

print("Bienvenido al reproductor musical PyArd")

# Variable global para almacenar el resultado del inicio de sesión
resultado_usuario = None

def menu_principal():
    print("------------------------------------------------")
    print("Seleccione alguna de las siguientes opciones: ")
    print("1. Ingresar cuenta existente")
    print("2. Registrarse")
    print("3. Salir de la aplicación")
    print("------------------------------------------------")

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
        print("------------------------------------------------")
        print("Usuario registrado con éxito.")
        print("------------------------------------------------")

    except Exception as e:
        print("------------------------------------------------")
        print(f"Error al registrar usuario: {e}")
        print("------------------------------------------------")

def ingresar():
    global resultado_usuario  # Hacer la variable global para almacenar el resultado del inicio de sesión
    user = input("Ingrese su usuario: ")
    password = input("Ingrese su contraseña: ")

    # Consulta parametrizada para verificar las credenciales
    query_usuario = "SELECT * FROM usuario WHERE nombre_user = %s AND contraseña = %s"
    datos_usuario = (user, password)

    try:
        cursor.execute(query_usuario, datos_usuario)
        resultado_usuario = cursor.fetchone()

        if resultado_usuario:
            print("------------------------------------------------")
            print("Inicio de sesión exitoso.")
            print("------------------------------------------------")

        else:
            print("------------------------------------------------")
            print("Credenciales incorrectas. Intente nuevamente.")
            print("------------------------------------------------")
    except Exception as e:
        print("------------------------------------------------")
        print(f"Error al ingresar: {e}")
        print("------------------------------------------------")

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

def reproducir_musica(archivo_musica):
    # Intenta abrir el reproductor predeterminado con la canción actual
    webbrowser.open(archivo_musica)

def ir_a_favoritos():
    if resultado_usuario:
        id_usuario = resultado_usuario[0]  # Obtener el ID del usuario
        query_favoritos = """
        SELECT c.id_cancion, c.nombre AS nombre_cancion, a.nombre AS nombre_artista, al.nombre AS nombre_album, g.nombre AS nombre_genero
        FROM lista_favoritos AS lf
        JOIN cancion AS c ON lf.id_cancion = c.id_cancion
        JOIN artista AS a ON c.id_artista = a.id_artista
        JOIN album AS al ON c.id_album = al.id_album
        JOIN generomusical AS g ON c.id_generomusical = g.id_generomusical
        WHERE lf.id_usuario = %s
        """
        cursor.execute(query_favoritos, (id_usuario,))
        favoritos = cursor.fetchall()

        if favoritos:
            print("Lista de favoritos:")
            for cancion in favoritos:
                print(cancion)

            while True:
                cancion_id = input("Seleccione la canción a escuchar (ingrese el ID) o 's' para salir: ")
                if cancion_id == 's':
                    principal()
                elif any(cancion[0] == int(cancion_id) for cancion in favoritos):
                    query_reproducir = "SELECT archivo_musica FROM cancion WHERE id_cancion = %s"
                    datos_reproducir = (cancion_id,)
                    cursor.execute(query_reproducir, datos_reproducir)
                    archivo_musica = cursor.fetchone()[0]
                    reproducir_musica(archivo_musica)
                else:
                    print("ID de canción no válido. Intente nuevamente.")
        
        else:
            print("No hay canciones en la lista de favoritos.")
    else:
        print("Inicia sesión para ver tus favoritos.")

def principal():
            if opcion == "1":
                ingresar()
                if resultado_usuario:
                    print("------------------------------------------------")
                    print("Opciones disponibles:")
                    print("1. Ir a la lista de favoritos")
                    print("2. Listar canciones")
                    print("3. Salir")
                    print("------------------------------------------------")

                    opcion_usuario = input("Ingrese el número de la opción deseada: ")

                    if opcion_usuario == "1":
                        print("------------------------------------------------")
                        ir_a_favoritos()
                        print("------------------------------------------------")
                    elif opcion_usuario == "2":
                        print("------------------------------------------------")
                        listar_canciones()
                        print("------------------------------------------------")
                        cancion_id = input("Seleccione la canción a escuchar (ingrese el ID): ")
                        query_reproducir = "SELECT archivo_musica FROM cancion WHERE id_cancion = %s"
                        datos_reproducir = (cancion_id,)
                        cursor.execute(query_reproducir, datos_reproducir)
                        archivo_musica = cursor.fetchone()[0]
                        reproducir_musica(archivo_musica)
                        agregar_lista = input("¿Desea agregarlo a su lista de reproducción? (si/no):")

                        if agregar_lista.lower() == 'si':
                        # Agregar la canción a la lista de favoritos
                            if resultado_usuario:
                                id_usuario = resultado_usuario[0]
                                query_agregar_favorito = "INSERT INTO lista_favoritos (id_usuario, id_cancion) VALUES (%s, %s)"
                                datos_agregar_favorito = (id_usuario, cancion_id)
                                try:
                                    cursor.execute(query_agregar_favorito, datos_agregar_favorito)
                                    conexion.commit()
                                    print("------------------------------------------------")
                                    print("Canción agregada a la lista de favoritos.")
                                    print("------------------------------------------------")
                                except Exception as e:
                                    print("------------------------------------------------")
                                    print(f"Error al agregar a la lista de favoritos: {e}")
                                    print("------------------------------------------------")
                            else:
                                print("Inicia sesión para agregar canciones a tus favoritos.")                    
                elif opcion_usuario == "3":
                    salir()
                else:
                    print("Opción no válida. Intente nuevamente.")

            elif opcion == "2":
                print("------------------------------------------------")
                registrar_usuario()
                print("------------------------------------------------")

            elif opcion == "3":
                print("------------------------------------------------")
                salir()
                print("------------------------------------------------")
                
            else:
                print("------------------------------------------------")
                print("Opción no válida. Intente nuevamente.")
                print("------------------------------------------------")  

# Menú principal
while True:
    menu_principal()
    opcion = input("Ingrese el número de la opción deseada: ")
    if opcion == "1":
        principal()
    elif opcion == "2":
        print("------------------------------------------------")
        registrar_usuario()
        print("------------------------------------------------")
    elif opcion == "3":
        print("------------------------------------------------")
        salir()
        print("------------------------------------------------")
    else:
        print("------------------------------------------------")
        print("Opción no válida. Intente nuevamente.")
        print("------------------------------------------------")