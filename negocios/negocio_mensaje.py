from datos.conexion import Session
from sqlalchemy.exc import SQLAlchemyError
from modelos.usuario import Usuario
from modelos.mensaje import Mensaje

sesion = Session()

def valida_envia_mensaje(emisor, receptor):
    try:
        mensaje = input("Escribe tu mensaje: ")
        nuevo_mensaje = Mensaje(contenido_mensaje=mensaje, id_primer_usuario=emisor.id_usuario, id_segundo_usuario=receptor.id_usuario)
        sesion.add(nuevo_mensaje)
        sesion.commit()
        print("Mensaje enviado exitosamente")

    except SQLAlchemyError as e:
        sesion.rollback()
        print(f"Error: {e}")
