import Conexion
import pandas as pd
from sklearn.metrics import jaccard_score

# Crear un cursor
conexion = Conexion.establecer_conexion()
cursor = conexion.cursor()





def calcular_jaccard(lista1, lista2):
    # Calcular el coeficiente de Jaccard entre dos listas
    return jaccard_score(lista1, lista2)

def obtener_listas_favoritos():
    # Obtener las listas de canciones favoritas de los usuarios desde la tabla lista_favoritos
    # Realizar la consulta SQL correspondiente
    query_favoritos = """
    SELECT id_usuario, GROUP_CONCAT(id_cancion) AS canciones_favoritas
    FROM lista_favoritos
    GROUP BY id_usuario;
    """
    cursor.execute(query_favoritos)
    return cursor.fetchall()

def comparar_jaccard_y_leer_letras(favoritos):
    for i in range(len(favoritos)):
        for j in range(i + 1, len(favoritos)):
            usuario1, lista1 = favoritos[i]
            usuario2, lista2 = favoritos[j]
            # Calcular el coeficiente de Jaccard
            coeficiente_jaccard = calcular_jaccard(lista1.split(','), lista2.split(','))
            # Realizar un JOIN con la tabla de canciones para obtener la ubicación del archivo de letras
            query_join_canciones = f"""
            SELECT c.archivo_letra
            FROM cancion c
            JOIN lista_favoritos lf ON c.id_cancion = lf.id_cancion
            WHERE lf.id_usuario IN ({usuario1}, {usuario2});
            """
            cursor.execute(query_join_canciones)
            ubicaciones_letras = cursor.fetchall()

            # Leer las letras desde un archivo Excel (usando pandas como ejemplo)
            for ubicacion_letra in ubicaciones_letras:
                letra_df = pd.read_excel(ubicacion_letra[0])
                print(letra_df)

# Luego, puedes llamar a estas funciones en tu código principal:
favoritos = obtener_listas_favoritos()
comparar_jaccard_y_leer_letras(favoritos)
