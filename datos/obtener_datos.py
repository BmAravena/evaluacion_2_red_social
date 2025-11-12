from datos.conexion import sesion

# Función global para obtener datos de cualquier clase, se devuelve una lista con todos los datos para posteriormente ser utilizados
def obtener_datos(clase):
    datos = sesion.query(clase).all()
    if datos:    
            return datos
    else:
        print("no hay datos")
        return []   