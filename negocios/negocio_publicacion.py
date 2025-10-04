from datos.conexion import Session
from sqlalchemy.exc import SQLAlchemyError
from modelos.publicacion import Publicacion


sesion = Session()


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


        