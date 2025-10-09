from datos.conexion import Session
from sqlalchemy.exc import SQLAlchemyError
from modelos.usuario import Usuario
from modelos.mensaje import Mensaje
from prettytable import PrettyTable
from datos.obtener_datos import obtener_datos

sesion = Session()


def visualizar_mensajes(id):
    tabla_mensajes = PrettyTable()
    tabla_mensajes.field_names = ['contenido_mensaje', 'fecha_mensaje']

    mensajes = obtener_datos(Mensaje)

    if mensajes:
        for mensaje in mensajes:
            if mensaje.id_primer_usuario == id:
                tabla_mensajes.add_row([mensaje.contenido_mensaje, mensaje.fecha_mensaje])

    print(tabla_mensajes)

    

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
