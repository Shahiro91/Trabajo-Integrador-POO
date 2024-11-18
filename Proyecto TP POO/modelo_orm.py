from peewee import *

# base de datos SQLite
db = SqliteDatabase('obras_urbanas.db')


class BaseModel(Model):
    class Meta:
        database = db

class Obra(BaseModel):
    nombre = CharField()
    direccion = CharField()
    estado = CharField()
    fecha_inicio = DateField()
    fecha_fin = DateField(null=True)  
    monto = FloatField()
    empresa_constructora = CharField()
    cuit = CharField()
    descripcion = TextField()
    ubicacion = CharField()
    ministerio_responsable = CharField()

# tablas en la base de datos
def crear_tablas():
    try:
        db.connect()
        db.create_tables([Obra])
        print("Tablas creadas con éxito.")
    except Exception as e:
        print(f"Error al crear las tablas: {e}")
    
    finally:
        # Cerrar la conexión
        if not db.is_closed():
            db.close()
            print("Conexión cerrada.")

# Ejecutar tablas
if __name__ == "__main__":
    crear_tablas()
