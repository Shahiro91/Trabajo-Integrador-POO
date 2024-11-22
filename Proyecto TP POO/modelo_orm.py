from peewee import Model, CharField, FloatField, DateField, ForeignKeyField, SqliteDatabase

# Conexión a la base de datos SQLite
db = SqliteDatabase('obras_urbanas.db')

class BaseModel(Model):
    class Meta:
        database = db

class Etapa(BaseModel):
    nombre = CharField()

class FuenteFinanciamiento(BaseModel):
    nombre = CharField()

class Empresa(BaseModel):
    nombre = CharField()

class Obra(BaseModel):
    nombre = CharField()
    direccion = CharField()
    estado = CharField()
    fecha_inicio = DateField()
    fecha_fin = DateField(null=True)
    monto = FloatField()
    empresa_constructora = ForeignKeyField(Empresa)
    cuit = CharField()
    descripcion = CharField()
    ubicacion = CharField()
    ministerio_responsable = CharField()
    etapa = ForeignKeyField(Etapa)
    fuente_financiamiento = ForeignKeyField(FuenteFinanciamiento)
    mano_obra = FloatField()

    def nuevo_proyecto(self):
        etapa = Etapa.get(Etapa.nombre == "Proyecto")
        self.etapa = etapa
        self.save()

    def iniciar_contratacion(self, tipo_contratacion, nro_contratacion):
        # Implementar lógica de contratación
        pass

    def adjudicar_obra(self, empresa, nro_expediente):
        # Implementar adjudicación de la obra
        pass

    def iniciar_obra(self, destacada, fecha_inicio, fecha_fin_inicial, fuente_financiamiento, mano_obra):
        # Implementar inicio de obra
        pass

    def actualizar_porcentaje_avance(self, porcentaje_avance):
        self.monto = porcentaje_avance
        self.save()

    def incrementar_plazo(self, plazo_meses):
        # Implementar incremento de plazo
        pass

    def incrementar_mano_obra(self, cantidad):
        # Implementar incremento de mano de obra
        pass

    def finalizar_obra(self):
        self.etapa = Etapa.get(Etapa.nombre == "Finalizada")
        self.save()

    def rescindir_obra(self):
        self.etapa = Etapa.get(Etapa.nombre == "Rescindida")
        self.save()
