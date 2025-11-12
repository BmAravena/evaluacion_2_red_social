from datos.conexion import sesion
from sqlalchemy.exc import SQLAlchemyError
from modelos.publicacion import Publicacion
from datos.obtener_datos import obtener_datos
from prettytable import PrettyTable


# Visualizar las publicaciones, primero creamos una tabla
def visualizar_publicaciones():
    tabla_publicaciones = PrettyTable()
    tabla_publicaciones.field_names = ['contenido_publicacion', 'fecha_publicacion']
    # Obtenemos una lista de publicaciones
    publicaciones = obtener_datos(Publicacion)
    # Si hay publicaciones
    if publicaciones:
        # Iteramos las publicsciones y las agregamos a la tabla
        for publicacion in publicaciones:
            tabla_publicaciones.add_row([publicacion.contenido_publicacion, publicacion.fecha_publicacion])

    print(tabla_publicaciones)

# Validamos la publicación, primero obtenemos un usuario
def valida_publicacion(usuario):
    # Se pide el contenido de la publicación y instanciamos una nueva publicación
    try:
        publi = input("Ingresa lo que deseas publicar: ")
        nueva_publicacion = Publicacion(contenido_publicacion=publi, id_usuario=usuario.id_usuario)
        sesion.add(nueva_publicacion)
        sesion.commit()
        print("Públicación creada exitosamente")

    except SQLAlchemyError as e:
        sesion.rollback()
        print(f"Error: {e}")


        