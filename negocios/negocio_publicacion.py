from datos.conexion import Session
from sqlalchemy.exc import SQLAlchemyError
from modelos.publicacion import Publicacion
from datos.obtener_datos import obtener_datos
from prettytable import PrettyTable


sesion = Session()


def visualizar_publicaciones():
    tabla_publicaciones = PrettyTable()
    tabla_publicaciones.field_names = ['contenido_publicacion', 'fecha_publicacion']

    publicaciones = obtener_datos(Publicacion)

    if publicaciones:
        for publicacion in publicaciones:
            tabla_publicaciones.add_row([publicacion.contenido_publicacion, publicacion.fecha_publicacion])

    print(tabla_publicaciones)


def valida_publicacion(usuario):
    try:
        publi = input("Ingresa lo que deseas publicar: ")
        nueva_publicacion = Publicacion(contenido_publicacion=publi, id_usuario=usuario.id_usuario)
        sesion.add(nueva_publicacion)
        sesion.commit()
        print("Públicación creada exitosamente")

    except SQLAlchemyError as e:
        sesion.rollback()
        print(f"Error: {e}")


        