from peewee import *
import datetime

# Definir la base de datos SQLite
db = SqliteDatabase('obras_urbanas.db')

# Clase base para el modelo ORM
class BaseModel(Model):
    class Meta:
        database = db

class Obra(BaseModel):
    nombre = CharField()
    tipo_obra = CharField()
    area_responsable = CharField()
    barrio = CharField()
    etapa = CharField()
    porcentaje_avance = IntegerField(default=0)
    plazo_meses = IntegerField(default=0)
    mano_obra = IntegerField(default=0)
    fecha_inicio = DateField(null=True)
    fecha_fin_inicial = DateField(null=True)
    destacada = BooleanField(default=False)
    fuente_financiamiento = CharField(null=True)
    nro_contratacion = CharField(null=True)
    empresa = CharField(null=True)
    nro_expediente = CharField(null=True)

    def nuevo_proyecto(self):
        self.etapa = 'Proyecto'
        self.save()

    def iniciar_contratacion(self, tipo_contratacion, nro_contratacion):
        self.etapa = 'Contratación'
        self.tipo_contratacion = tipo_contratacion
        self.nro_contratacion = nro_contratacion
        self.save()

    def adjudicar_obra(self, empresa, nro_expediente):
        self.etapa = 'Adjudicada'
        self.empresa = empresa
        self.nro_expediente = nro_expediente
        self.save()

    def iniciar_obra(self, destacada, fecha_inicio, fecha_fin_inicial, fuente_financiamiento, mano_obra):
        self.etapa = 'En Ejecución'
        self.destacada = destacada
        self.fecha_inicio = fecha_inicio
        self.fecha_fin_inicial = fecha_fin_inicial
        self.fuente_financiamiento = fuente_financiamiento
        self.mano_obra = mano_obra
        self.save()

    def actualizar_porcentaje_avance(self, porcentaje_avance):
        self.porcentaje_avance = porcentaje_avance
        self.save()

    def incrementar_plazo(self, plazo_meses):
        self.plazo_meses += plazo_meses
        self.save()

    def incrementar_mano_obra(self, mano_obra):
        self.mano_obra += mano_obra
        self.save()

    def finalizar_obra(self):
        self.etapa = 'Finalizada'
        self.porcentaje_avance = 100
        self.save()

    def rescindir_obra(self):
        self.etapa = 'Rescindida'
        self.save()
