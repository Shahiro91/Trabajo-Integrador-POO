import pandas as pd
from modelo_orm import *

class GestionarObra:
    
    df = None  # Definir df como un atributo de clase

    @classmethod
    def extraer_datos(cls, file_path):
        try:
            cls.df = pd.read_csv(file_path, encoding='latin1', on_bad_lines='skip')
            return cls.df
        except Exception as e:
            print(f"Error al extraer datos: {e}")


    @classmethod
    def conectar_db(cls):
        try:
            db.connect()
        except Exception as e:
            print(f"Error al conectar a la base de datos: {e}")

    @classmethod
    def mapear_orm(cls):
        try:
            db.create_tables([Obra])
        except Exception as e:
            print(f"Error al crear las tablas: {e}")

    @classmethod
    def limpiar_datos(cls):
        try:
            if cls.df is not None:
                cls.df.dropna(inplace=True)
            else:
                print("Error: DataFrame no definido")
        except Exception as e:
            print(f"Error al limpiar los datos: {e}")

    @classmethod
    def cargar_datos(cls):
        try:
            if cls.df is not None:
                for _, row in cls.df.iterrows():
                    Obra.create(
                        nombre=row['nombre'],
                        tipo_obra=row['tipo_obra'],
                        area_responsable=row['area_responsable'],
                        barrio=row['barrio'],
                        etapa=row['etapa'],
                        porcentaje_avance=row['porcentaje_avance'],
                        plazo_meses=row['plazo_meses'],
                        mano_obra=row['mano_obra'],
                        fecha_inicio=row['fecha_inicio'],
                        fecha_fin_inicial=row['fecha_fin_inicial'],
                        destacada=row['destacada'],
                        fuente_financiamiento=row['fuente_financiamiento'],
                        nro_contratacion=row['nro_contratacion'],
                        empresa=row['empresa'],
                        nro_expediente=row['nro_expediente']
                    )
            else:
                print("Error: DataFrame no definido")
        except Exception as e:
            print(f"Error al cargar los datos: {e}")

    @classmethod
    def nueva_obra(cls):
        try:
            nombre = input("Nombre de la obra: ")
            tipo_obra = input("Tipo de obra: ")
            area_responsable = input("Área responsable: ")
            barrio = input("Barrio: ")
            obra = Obra.create(
                nombre=nombre,
                tipo_obra=tipo_obra,
                area_responsable=area_responsable,
                barrio=barrio,
                etapa='Proyecto'
            )
            obra.save()
            return obra
        except Exception as e:
            print(f"Error al crear nueva obra: {e}")

    @classmethod
    def obtener_indicadores(cls):
        try:
            print("Listado de todas las áreas responsables:")
            areas_responsables = Obra.select(Obra.area_responsable).distinct()
            for area in areas_responsables:
                print(area.area_responsable)

            print("\nListado de todos los tipos de obra:")
            tipos_obra = Obra.select(Obra.tipo_obra).distinct()
            for tipo in tipos_obra:
                print(tipo.tipo_obra)
            
            # Aquí puedes seguir añadiendo los indicadores restantes de acuerdo a los requisitos del proyecto
        except Exception as e:
            print(f"Error al obtener indicadores: {e}")

# Ejemplo de uso
if __name__ == "__main__":
    GestionarObra.conectar_db()
    GestionarObra.mapear_orm()
    df = GestionarObra.extraer_datos("observatorio-de-obras-urbanas.csv")
    GestionarObra.limpiar_datos()
    GestionarObra.cargar_datos()
    GestionarObra.obtener_indicadores()
