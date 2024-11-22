from gestionar_obras import GestionarObraConcreta

# Configuración inicial
GestionarObraConcreta.mapear_orm()

# Creación de una instancia para gestionar obras
gestor = GestionarObraConcreta()

# Ruta del archivo CSV
ruta_csv = "observatorio-de-obras-urbanas.csv"  # Asegúrate de que el archivo existe y tiene los datos correctos

# Extraer, limpiar y cargar los datos
datos = gestor.extraer_datos(ruta_csv)
datos_limpios = gestor.limpiar_datos(datos)
gestor.cargar_datos(datos_limpios)

# Mostrar registros cargados
gestor.mostrar_registros()



