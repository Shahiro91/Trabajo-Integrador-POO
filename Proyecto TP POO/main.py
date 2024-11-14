from gestionar_obras import GestionarObra

def main():
    # Conectar a la base de datos
    GestionarObra.conectar_db()
    
    # Crear la estructura de la base de datos
    GestionarObra.mapear_orm()
    
    # Extraer datos del archivo Excel
    df = GestionarObra.extraer_datos("observatorio-de-obras-urbanas.xlsx")
    
    # Limpiar los datos
    GestionarObra.limpiar_datos()
    
    # Cargar los datos en la base de datos
    GestionarObra.cargar_datos()
    
    # Crear nuevas instancias de Obra (este es solo un ejemplo, puedes adaptarlo según necesites)
    nueva_obra = GestionarObra.nueva_obra()
    nueva_obra.nuevo_proyecto()
    nueva_obra.iniciar_contratacion('TipoContratacionEjemplo', 'NroContratacionEjemplo')
    nueva_obra.adjudicar_obra('EmpresaEjemplo', 'NroExpedienteEjemplo')
    nueva_obra.iniciar_obra(True, '2024-01-01', '2024-12-31', 'FuenteFinanciamientoEjemplo', 10)
    nueva_obra.actualizar_porcentaje_avance(50)
    nueva_obra.finalizar_obra()
    
    # Obtener indicadores y mostrar en consola
    GestionarObra.obtener_indicadores()

if __name__ == "__main__":
    main()






