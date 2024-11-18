import pandas as pd
import sqlite3
from peewee import SqliteDatabase
from abc import ABC, abstractmethod

# Clase abstracta GestionarObra
class GestionarObra(ABC):

    @abstractmethod
    def extraer_datos(self):
        pass
    
    @abstractmethod
    def conectar_db(self):
        pass


# Subclase que implementa los métodos de GestionarObra
class GestionarObraConcreta(GestionarObra):
    def __init__(self):
        self.db = SqliteDatabase('obras_urbanas.db')
        self.dataset = None  

    def extraer_datos(self):
        
        try:
            self.dataset = pd.read_csv('observatorio-de-obras-urbanas.csv', encoding='latin 1')
            print("Datos extraídos con éxito")
        except Exception as e:
            print(f"Error al extraer los datos: {e}")

    def conectar_db(self):
        try:
            if not self.db.is_closed():
                print("La conexión ya está abierta.")
            else:
                self.db.connect()
            print("Conexión a la base de datos establecida con éxito.")
        except Exception as e:
            print(f"Error al conectar a la base de datos: {e}")

    def cerrar_db(self):
        if not self.db.is_closed():
            self.db.close()
            print("Conexión cerrada.")
        else:
            print("La base de datos ya está cerrada.")

