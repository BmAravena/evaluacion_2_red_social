from datos.conexion import Session

sesion = Session()


def obtener_datos(clase):
    datos = sesion.query(clase).all()
    if datos:    
            return datos
    else:
        print("no hay datos")