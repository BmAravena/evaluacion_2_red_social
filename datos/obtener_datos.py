from datos.conexion import sesion


def obtener_datos(clase):
    datos = sesion.query(clase).all()
    if datos:    
            return datos
    else:
        print("no hay datos")
        return []   