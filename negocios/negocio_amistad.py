from datos.conexion import Session
from sqlalchemy.exc import SQLAlchemyError
from modelos.amistad import Amistad
from modelos.usuario import Usuario
from sqlalchemy import or_, and_
from datos.obtener_datos import obtener_datos


sesion = Session()


def valida_amistad(emisor, receptor):
    amistad = Amistad
    amistades = obtener_datos(amistad)
    for am in amistades:
        if (am.id_primer_usuario == emisor.id_usuario and am.id_segundo_usuario == receptor.id_usuario) or (am.id_primer_usuario == receptor.id_usuario and am.id_segundo_usuario == emisor.id_usuario):
            return True, am
        
    return False


def enviar_solicitud(id_emisor, id_receptor):
    if not id_emisor == id_receptor:
        existente = (
        sesion.query(Amistad)
        .filter(
            or_(
                and_(Amistad.id_primer_usuario == id_emisor, Amistad.id_segundo_usuario == id_receptor),
                and_(Amistad.id_primer_usuario == id_receptor, Amistad.id_segundo_usuario == id_emisor)
            )
        )
        .first() )

        if not existente:
            solicitud = Amistad(id_primer_usuario=id_emisor, id_segundo_usuario=id_receptor, estado="pendiente")
            sesion.add(solicitud)
            sesion.commit()
            print("Solicitud de amistad enviada")
            return id_emisor
        else:
            print("Error, ya existe amistad")
    else:
        print("No puedos enviarte solicitud a tí mismo")



def responder_solicitud(id_receptor):

    while True:
        # Obtener todas las solicitudes y filtrar pendientes para este usuario
        solicitudes = obtener_datos(Amistad)
        pendientes = [
            s for s in solicitudes
            if s.id_segundo_usuario == id_receptor and s.estado.lower().strip() == "pendiente"
        ]

        if not pendientes:
            print("No tienes más solicitudes pendientes.")
            break  # Salir del bucle cuando no queden pendientes

        # Procesar la primera solicitud pendiente
        solicitud = pendientes[0]

        # Buscar usuario que envió la solicitud
        usuarios_filtrados = [
            u for u in obtener_datos(Usuario) if u.id_usuario == solicitud.id_primer_usuario
        ]

        if not usuarios_filtrados:
            print(f"No se encontró el usuario que envió la solicitud con ID {solicitud.id_primer_usuario}.")
            # Marcar la solicitud como "rechazada automáticamente" o saltar
            solicitud.estado = "rechazada"
            sesion.commit()
            continue

        usuario = usuarios_filtrados[0]

        # Preguntar al receptor si acepta o rechaza
        confirmar = input(
            f"{usuario.nombre_usuario} te ha enviado una solicitud de amistad. ¿Deseas aceptar? (si/no): "
        ).strip().lower()

        if confirmar == "si":
            solicitud.estado = "aceptada"
            print(f"Solicitud aceptada. Ahora eres amigo de {usuario.nombre_usuario}.")
        elif confirmar == "no":
            solicitud.estado = "rechazada"
            print(f"Solicitud rechazada de {usuario.nombre_usuario}.")
        else:
            print("Respuesta no válida. La solicitud se mantiene pendiente.")
            continue  # No commit, vuelve a preguntar si quieres

        # Guardar cambios en la DB inmediatamente
        try:
            sesion.commit()
        except Exception as e:
            sesion.rollback()
            print(f"Error al guardar cambios: {e}")
            break


 