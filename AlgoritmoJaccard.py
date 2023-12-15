import Conexion
import sys
import numpy as np

# Crear un cursor
conexion2 = Conexion.establecer_conexion()
cursor2 = conexion2.cursor()

# Función para mostrar el menú de opciones
def menu_algoritmo():
    print("-------------------------------------------")
    print("Seleccione una de las siguientes opciones: ")
    print("1. Ver similaridades entre los usuarios")
    print("2. Ver cómo funciona el algoritmo")
    print("3. Ver letras almacenadas por un usuario específico")
    print("4. Ver matriz de similitud entre usuarios")
    print("5. Salir")
    print("6. Recomendación musical")
    print("-------------------------------------------")

# Función para hallar el coeficiente de Jaccard
def algoritmo_Jaccard(id_usuario1, id_usuario2):
    palabras_usuario1 = set(listas_palabras_por_usuario.get(id_usuario1, []))
    palabras_usuario2 = set(listas_palabras_por_usuario.get(id_usuario2, []))

    # Realizar el cálculo del coeficiente de Jaccard con las palabras de ambos usuarios
    interseccion = len(palabras_usuario1.intersection(palabras_usuario2))
    union = len(palabras_usuario1.union(palabras_usuario2))

    # Calcular similitud de Jaccard y presentarlo como porcentaje redondeado a dos decimales
    coeficiente_jaccard = round((interseccion / union) * 100, 2) if union > 0 else 0
    print(f"Coeficiente de Jaccard entre Usuario {id_usuario1} y Usuario {id_usuario2}: {coeficiente_jaccard}%")
    return coeficiente_jaccard

# Función para recomendar canciones basadas en el coeficiente de Jaccard
def recomendacion_musical(id_usuario1, id_usuario2):
    coeficiente_jaccard = algoritmo_Jaccard(id_usuario1, id_usuario2)

    if coeficiente_jaccard >= 50.00:
        print(f"¡Recomendación musical para Usuarios {id_usuario1} y {id_usuario2}!")

        # Obtener las canciones escuchadas por cada usuario
        canciones_usuario1 = set(obtener_canciones_escuchadas(id_usuario1))
        canciones_usuario2 = set(obtener_canciones_escuchadas(id_usuario2))

        # Encontrar canciones que no tienen en común ambos usuarios
        canciones_no_comunes = canciones_usuario1.symmetric_difference(canciones_usuario2)

        # Agregar las canciones no comunes a la tabla lista_recomendacion
        for id_cancion in canciones_no_comunes:
            agregar_cancion_a_lista_recomendacion(id_usuario1, id_cancion)

        print("Canciones recomendadas agregadas a lista_recomendacion.")
    else:
        print(f"No hay suficiente similitud para recomendar canciones entre Usuarios {id_usuario1} y {id_usuario2}.")

# Función para obtener las canciones escuchadas por un usuario
def obtener_canciones_escuchadas(id_usuario):
    query_canciones_escuchadas = """
        SELECT id_cancion
        FROM cancion_escuchada
        WHERE id_usuario = %s;
    """
    cursor2.execute(query_canciones_escuchadas, (id_usuario,))
    canciones = cursor2.fetchall()
    return [cancion[0] for cancion in canciones]

# Función para agregar canción a lista_recomendacion
def agregar_cancion_a_lista_recomendacion(id_usuario, id_cancion):
    query_agregar_cancion = """
        INSERT INTO lista_recomendacion (id_usuario, id_cancion)
        VALUES (%s, %s)
    """
    cursor2.execute(query_agregar_cancion, (id_usuario, id_cancion))
    conexion2.commit()

# Función para obtener el id de la lista de favoritos de un usuario
def obtener_id_lista_favoritos(id_usuario):
    query_id_lista_favoritos = """
        SELECT id_lista_favoritos
        FROM lista_favoritos
        WHERE id_usuario = %s;
    """
    cursor2.execute(query_id_lista_favoritos, (id_usuario,))
    result = cursor2.fetchone()
    return result[0] if result else None

# Función para mostrar la metodología del coeficiente de Jaccard
def metodologia_Jaccard():
    # Explicar la metodología utilizando las listas de palabras
    pass

# Función para leer las letras almacenadas por un usuario específico
def archivo_letra(id_usuario):
    query_favoritos = """
        SELECT cancion.archivo_letra
        FROM cancion
        JOIN cancion_escuchada ON cancion.id_cancion = cancion_escuchada.id_cancion
        WHERE cancion_escuchada.id_usuario = %s;
    """
    cursor2.execute(query_favoritos, (id_usuario,))
    favoritos = cursor2.fetchall()

    palabras = []  # Lista para almacenar las palabras de los archivos

    for archivo in favoritos:
        archivo_path = archivo[0]  # Supongo que el nombre del archivo está en la primera columna
        try:
            with open(archivo_path, "rt", encoding="utf-8") as archivo_letra:
                contenido = archivo_letra.read()
                palabras.extend(contenido.split())  # Agregar cada palabra a la lista
        except UnicodeDecodeError as e:
            print(f"Error al decodificar el archivo {archivo_path}: {e}")

    return palabras

# Función para mostrar las letras almacenadas por un usuario específico
def ver_letras_usuario_especifico():
    id_usuario = int(input("Ingrese el ID del usuario para ver las letras almacenadas: "))
    palabras_usuario = listas_palabras_por_usuario.get(id_usuario, [])
    print(f"Letras almacenadas por Usuario {id_usuario}: {palabras_usuario}")

# Función para crear la matriz de similitud entre usuarios usando Jaccard
def matriz_similitud_jaccard(usuarios):
    matriz_similitud = np.zeros((len(usuarios), len(usuarios)))

    for i in range(len(usuarios)):
        for j in range(i + 1, len(usuarios)):
            id_usuario1 = usuarios[i]
            id_usuario2 = usuarios[j]

            palabras_usuario1 = set(listas_palabras_por_usuario.get(id_usuario1, []))
            palabras_usuario2 = set(listas_palabras_por_usuario.get(id_usuario2, []))

            # Calcular similitud de Jaccard
            interseccion = len(palabras_usuario1.intersection(palabras_usuario2))
            union = len(palabras_usuario1.union(palabras_usuario2))

            # Evitar la división por cero
            coeficiente_jaccard = round((interseccion / union) * 100, 2) if union > 0 else 0

            matriz_similitud[i, j] = coeficiente_jaccard
            matriz_similitud[j, i] = coeficiente_jaccard

    return matriz_similitud

# Obtener las listas de palabras para cada usuario
usuarios = [1, 2, 3, 4, 5,6,7]
listas_palabras_por_usuario = {}

for id_usuario in usuarios:
    lista_palabras = archivo_letra(id_usuario)
    listas_palabras_por_usuario[id_usuario] = lista_palabras

def salir():
    cursor2.close()
    Conexion.cerrar_conexion(conexion2)
    sys.exit()

# Bucle principal del programa
while True:
    menu_algoritmo()
    opcion = input("Ingresa una de las siguientes opciones: ")

    if opcion == "1":
        id_usuario1 = int(input("Ingrese el ID del primer usuario: "))
        id_usuario2 = int(input("Ingrese el ID del segundo usuario: "))
        algoritmo_Jaccard(id_usuario1, id_usuario2)
    elif opcion == "2":
        metodologia_Jaccard()
    elif opcion == "3":
        ver_letras_usuario_especifico()
    elif opcion == "4":
        matriz = matriz_similitud_jaccard(usuarios)
        # Imprimir la matriz junto con los identificadores de usuario
        print("     " + "     ".join(map(str, usuarios)))
        for i, row in zip(usuarios, matriz):
            print(f"{i}  {row}")
    elif opcion == "5":
        salir()
    elif opcion == "6":  # Nueva opción para recomendación musical
        id_usuario1 = int(input("Ingrese el ID del primer usuario: "))
        id_usuario2 = int(input("Ingrese el ID del segundo usuario: "))
        recomendacion_musical(id_usuario1, id_usuario2)
    else:
        print("Opción no válida. Inténtalo de nuevo.")
