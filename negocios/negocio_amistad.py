from datos.conexion import Session
from sqlalchemy.exc import SQLAlchemyError
from modelos.amistad import Amistad
from modelos.usuario import Usuario

sesion = Session()



def enviar_solicitud(id_emisor, id_receptor):
    if not id_emisor == id_receptor:
        existente = sesion.query(Amistad).filter_by(id_primer_usuario=id_emisor, id_segundo_usuario=id_receptor).first()

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



def responder_solicitud(id_amistad, aceptar=True):
    solicitud = sesion.query(Amistad).filter_by(id=id_amistad).first()

    if solicitud:
        if aceptar:
            solicitud.estado = "aceptada"
        else:
            solicitud.estado = "rechazada"
      
        sesion.commit()
        print(f"Solicitud aceptada")

    else:
        print("No se encontró la solicitud")


