from datos.conexion import sesion
from sqlalchemy.exc import SQLAlchemyError
from modelos.comentario import Comentario


# Función para validar comentario y comentar, primero recibimos una publicación y un usuario
def valida_comentario(publicacion, usuario):
    # Luego pedimos el contenido del comentario y instanciamos un nuevo comentario
    try:
        coment = input("Ingresa lo que deseas comentar: ")
        nuevo_comentario = Comentario(comentario=coment, id_publicacion=publicacion.id_publicacion, id_usuario=usuario.id_usuario)
        sesion.add(nuevo_comentario)
        sesion.commit()
        print("Comentario realizado exitosamente")

    except SQLAlchemyError as e:
        sesion.rollback()
        print(f"Error: {e}")