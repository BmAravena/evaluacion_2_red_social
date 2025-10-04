from datos.conexion import Session
from sqlalchemy.exc import SQLAlchemyError
from modelos.comentario import Comentario


sesion = Session()


def valida_comentario(publicacion, usuario):
    try:
        coment = input("Ingresa lo que deseas comentar: ")
        nuevo_comentario = Comentario(comentario=coment, id_publicacion=publicacion.id_publicacion, id_usuario=usuario.id_usuario)
        sesion.add(nuevo_comentario)
        sesion.commit()
        print("Comentario realizado exitosamente")

    except SQLAlchemyError as e:
        sesion.rollback()
        print(f"Error: {e}")