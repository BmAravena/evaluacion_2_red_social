from datos.conexion import Session
from sqlalchemy.exc import SQLAlchemyError
from modelos.amistad import Amistad
from modelos.usuario import Usuario
from sqlalchemy import or_, and_

sesion = Session()



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



def responder_solicitud(id_receptor, aceptar=True):
    solicitud = sesion.query(Amistad).filter_by(id_segundo_usuario=id_receptor).first()
 
    if solicitud:
        #estado = sesion.query(Amistad).filter_by(estado="pendiente").first()
        msg = ""
        if solicitud.estado == 'pendiente':
            usuario = sesion.query(Usuario).filter_by(id_usuario=solicitud.id_primer_usuario).first()

            confirmar = input(f"{usuario.nombre_usuario} te ha enviado una solicitud de amistad, ¿Deseas aceptar la solicitud de amistad?: ")

            if confirmar == 'si':
                solicitud.estado = "aceptada"
                print(f"Solicitud aceptada, ahora eres amigo de {usuario.nombre_usuario}")
                
            elif confirmar == "no":
                solicitud.estado = "rechazada"
                print(f"Solicitud rechazada")

            else:
                print("Respuesta no válida")

            sesion.commit()


        else:
            print("Esta solicitud no está pendiente")

    else:
        print("No tines solicitudes pendientes")