import tkinter as tk
from tkinter import messagebox
import pygame
import sys
import mysql.connector as mysql

class ReproductorMusicalGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Reproductor Musical")
        
        self.conexion = self.establecer_conexion()
        self.cursor = self.conexion.cursor()

        self.ingresar_btn = tk.Button(self.master, text="Ingresar", command=self.ingresar)
        self.ingresar_btn.pack()

        self.registrar_btn = tk.Button(self.master, text="Registrarse", command=self.registrarse)
        self.registrar_btn.pack()

        self.listar_canciones_btn = tk.Button(self.master, text="Listar Canciones", command=self.listar_canciones)
        self.listar_canciones_btn.pack()

        self.salir_btn = tk.Button(self.master, text="Salir", command=self.salir)
        self.salir_btn.pack()

    def establecer_conexion(self):
        try:
            conexion = mysql.connect(
                user='root',
                password='12345678',
                host='localhost',
                database='db_reproductormusical',
                port='3306'
            )
            print("Conexión exitosa.")
            return conexion
        except mysql.Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            sys.exit()

    def ingresar(self):
        user = input("Ingrese su usuario: ")
        password = input("Ingrese su contraseña: ")
        query_usuario = "SELECT * FROM usuario WHERE nombre_user = %s AND contraseña = %s"
        datos_usuario = (user, password)
        try:
            self.cursor.execute(query_usuario, datos_usuario)
            resultado_usuario = self.cursor.fetchone()

            if resultado_usuario:
                print("Inicio de sesión exitoso.")
            else:
                print("Credenciales incorrectas. Intente nuevamente.")
        except Exception as e:
            print(f"Error al ingresar: {e}")

    def registrarse(self):
        nombre = input("Ingresar nombre: ")
        apellido = input("Ingresar apellidos: ")
        sexo = input("Ingrese su género: ")
        fecha_nacimiento = input("Ingresar fecha de nacimiento (Año-mes-día): ")
        nacionalidad = input("Ingresar nacionalidad: ")
        correo = input("Ingresar correo electrónico: ")
        nombre_user = input("Cree su nombre de usuario: ")
        contraseña = input("Ingrese su contraseña: ")

        query = "INSERT INTO usuario(nombre, apellido, sexo, fecha_nacimiento, nacionalidad, correo, nombre_user, contraseña) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        datos_usuario = (nombre, apellido, sexo, fecha_nacimiento, nacionalidad, correo, nombre_user, contraseña)

        try:
            self.cursor.execute(query, datos_usuario)
            self.conexion.commit()
            print("Usuario registrado con éxito.")
        except Exception as e:
            print(f"Error al registrar usuario: {e}")

    def listar_canciones(self):
        query_canciones = """
        SELECT c.id_cancion, c.nombre AS nombre_cancion, a.nombre AS nombre_artista, al.nombre AS nombre_album, g.nombre AS nombre_genero
        FROM cancion AS c
        JOIN artista AS a ON c.id_artista = a.id_artista
        JOIN album AS al ON c.id_album = al.id_album
        JOIN generomusical AS g ON c.id_generomusical = g.id_generomusical;
        """
        self.cursor.execute(query_canciones)
        resultado_cancion = self.cursor.fetchone()
        while resultado_cancion:
            print(resultado_cancion)
            resultado_cancion = self.cursor.fetchone()        

    def salir(self):
        self.cursor.close()
        self.conexion.close()
        sys.exit()
        self.master.destroy()

class ReproductorMusical:
    def __init__(self):
        pygame.init()

    def reproducir_musica(self, archivo_musica):
        pygame.mixer.music.load(archivo_musica)
        pygame.mixer.music.play()

# Inicializar la aplicación
root = tk.Tk()
app = ReproductorMusicalGUI(root)
root.mainloop()
