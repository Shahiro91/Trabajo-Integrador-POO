from gestionar_obras import GestionarObraConcreta

def main():
    
    gestionar_obra = GestionarObraConcreta()
    gestionar_obra.extraer_datos()  
    gestionar_obra.conectar_db()    

if __name__ == "__main__":
    main()

