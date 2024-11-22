import pandas as pd
from modelo_orm import Obra, db
from normalizador import Normalizador

import pandas as pd



class GestionarObraConcreta:
    def __init__(self):
        self.dataset = None

    @staticmethod
    def conectar_db():
        try:
            db.connect()
            print("Conexión a la base de datos establecida.")
        except Exception as e:
            print(f"Error al conectar a la base de datos: {e}")

    @staticmethod
    def crear_tablas():
        try:
            with db:
                db.create_tables([Obra])
                print("Tablas creadas con éxito.")
        except Exception as e:
            print(f"Error al crear las tablas: {e}")

    @staticmethod
    def mapear_orm():
        try:
            GestionarObraConcreta.conectar_db()
            GestionarObraConcreta.crear_tablas()
            print("Mapeo ORM realizado con éxito.")
        except Exception as e:
            print(f"Error al mapear el ORM: {e}")

    def extraer_datos(self, ruta_csv):
        try:
             df = pd.read_csv(ruta_csv, encoding="latin1", sep=",", on_bad_lines='skip')
             print("Columnas:", df.columns)
             print(df.head())
        except Exception as e:
             print("Error al leer el CSV:", e)

    def limpiar_datos(self, datos):
        if datos is not None:
            try:
                datos.dropna(inplace=True)
                datos = Normalizador.aplicar_normalizacion(datos)
                print("Datos limpiados y normalizados con éxito.")
                return datos
            except Exception as e:
                print(f"Error al limpiar los datos: {e}")
                return None
        else:
            print("No hay datos cargados para limpiar.")
            return None

    def cargar_datos(self, datos):
        if datos is not None:
            try:
                for _, row in datos.iterrows():
                    Obra.create(
                        nombre=row['nombre'],
                        direccion=row['direccion'],
                        estado=row['estado'],
                        fecha_inicio=row['fecha_inicio'],
                        fecha_fin=row.get('fecha_fin', None),
                        monto=row['monto'],
                        empresa_constructora=row['empresa_constructora'],
                        cuit=row['cuit'],
                        descripcion=row['descripcion'],
                        ubicacion=row['ubicacion'],
                        ministerio_responsable=row['ministerio_responsable']
                    )
                print(f"{len(datos)} registros cargados con éxito.")
            except Exception as e:
                print(f"Error al cargar los datos en la base de datos: {e}")
        else:
            print("No hay datos para cargar en la base de datos.")

    @staticmethod
    def mostrar_registros():
        try:
            obras = Obra.select()
            for obra in obras:
                print(f"Obra: {obra.nombre}, Dirección: {obra.direccion}, Estado: {obra.estado}")
        except Exception as e:
            print(f"Error al mostrar los registros: {e}")

