from datos.conexion import sesion
from sqlalchemy.exc import SQLAlchemyError
from modelos.mensaje import Mensaje
from prettytable import PrettyTable
from datos.obtener_datos import obtener_datos


# Visualizamos los mensajes, primero creamos una tabla
def visualizar_mensajes(id):
    tabla_mensajes = PrettyTable()
    tabla_mensajes.field_names = ['contenido_mensaje', 'fecha_mensaje']
    # Obtenemos la lista de los mensajes
    mensajes = obtener_datos(Mensaje)
    # Si hay mensajes
    if mensajes:
        # Iteramos los mensajes y añadimos a la tabla únicamente los que cumplan con la id del usuario
        for mensaje in mensajes:
            if mensaje.id_primer_usuario == id:
                tabla_mensajes.add_row([mensaje.contenido_mensaje, mensaje.fecha_mensaje])

    print(tabla_mensajes)

    
# Validamos el envío de mensajes, primero recibimos dos usuarios
def valida_envia_mensaje(emisor, receptor):
    # Pedimos el contenido del mensaje y instanciamos un nuevo mensaje
    try:
        mensaje = input("Escribe tu mensaje: ")
        nuevo_mensaje = Mensaje(contenido_mensaje=mensaje, id_primer_usuario=emisor.id_usuario, id_segundo_usuario=receptor.id_usuario)
        sesion.add(nuevo_mensaje)
        sesion.commit()
        print("Mensaje enviado exitosamente")

    except SQLAlchemyError as e:
        sesion.rollback()
        print(f"Error: {e}")
