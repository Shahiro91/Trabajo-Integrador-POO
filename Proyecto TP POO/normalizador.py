import pandas as pd

class Normalizador:
    @staticmethod
    def normalizar_nombre(nombre):
        if pd.isna(nombre):
            return None
        return nombre.strip().lower().capitalize()
    
    @staticmethod
    def normalizar_cuit(cuit):
        if pd.isna(cuit):
            return None
        cuit = ''.join(filter(str.isdigit, str(cuit)))
        return cuit if len(cuit) == 11 else None
    
    @staticmethod
    def normalizar_fecha(fecha):
        try:
            return pd.to_datetime(fecha).strftime('%Y-%m-%d')
        except Exception:
            return None
    
    @staticmethod
    def normalizar_monto(monto):
        try:
            return float(str(monto).replace('$', '').strip())
        except ValueError:
            return None
     
    @staticmethod
    def aplicar_normalizacion(dataframe):
        # Verifica que las columnas existan antes de intentar normalizarlas
        if 'nombre' in dataframe.columns:
            dataframe['nombre'] = dataframe['nombre'].apply(Normalizador.normalizar_nombre)
        if 'cuit' in dataframe.columns:
            dataframe['cuit'] = dataframe['cuit'].apply(Normalizador.normalizar_cuit)
        if 'fecha_inicio' in dataframe.columns:
            dataframe['fecha_inicio'] = dataframe['fecha_inicio'].apply(Normalizador.normalizar_fecha)
        if 'fecha_fin' in dataframe.columns:
            dataframe['fecha_fin'] = dataframe['fecha_fin'].apply(Normalizador.normalizar_fecha)
        if 'monto' in dataframe.columns:
            dataframe['monto'] = dataframe['monto'].apply(Normalizador.normalizar_monto)
        return dataframe
