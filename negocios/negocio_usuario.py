from datos.conexion import Session
from sqlalchemy.exc import SQLAlchemyError
from modelos.usuario import Usuario
from modelos.publicacion import Publicacion
from negocios.negocio_publicacion import valida_publicacion
from negocios.negocio_comentario import valida_comentario
from negocios.negocio_amistad import enviar_solicitud, responder_solicitud
from auxiliares.info_app import nombre_aplicacion

sesion = Session()
    
def validador_de_identidad():
    nombre_usuario = input("Ingresa tu nombre de usuario: ")
    usuario = sesion.query(Usuario).filter_by(nombre_usuario=nombre_usuario).first()

def registrar_usuario():
    usuario = input("Ingresa nombre de usuario: ")
    existe_usuario = sesion.query(Usuario).filter_by(nombre_usuario=usuario).first()
    if not existe_usuario:
        mail = input("Ingresa el correo: ")
        existe_correo = sesion.query(Usuario).filter_by(correo=mail).first()
        if not existe_correo:
            contrasenha = input("Ingresa una contraseña: ")
            nuevo_usuario = Usuario(nombre_usuario=usuario, contrasenha=contrasenha, correo=mail)
            try:
                sesion.add(nuevo_usuario)
                sesion.commit()
                print("El usuario ha sido registrado exitosamente")
                
            except SQLAlchemyError as e:
                sesion.rollback()  # Revertir cambios si ocurre error
                print("Error al registrar el usuario:", e)

        else:
            print("Este correo ya está registrado, por favor intentálo nuevamente")
    else:
        print("Este nombre de usuario ya está registrado, por favor intentálo nuevamente")




def realizar_publicacion():
    nombre_usuario = input("Ingresa tu nombre de usuario: ")
    usuario = sesion.query(Usuario).filter_by(nombre_usuario=nombre_usuario).first()
    if usuario:
        valida_publicacion(usuario)
    else:
        print("Este usuario no existe, por favor intentálo nuevamente")




def realizar_comentario():
    nombre_usuario = input("Ingresa tu nombre de usuario: ")
    usuario = sesion.query(Usuario).filter_by(nombre_usuario=nombre_usuario).first()
    if usuario:
        id_publi = int(input("Ingresa la ID de la públicación a comentar: "))
        publicacion = sesion.query(Publicacion).filter_by(id_publicacion=id_publi).first()
        if publicacion:
            valida_comentario(publicacion, usuario)
        else: 
            print("Esa públicación no existe, intentálo nuevamente")
    else:
        print("Este usuario no existe, por favor intentálo nuevamente")




def enviar_solicitud_amistad():
    nombre_usuario = input("Ingresa tu nombre de usuario: ")
    usuario = sesion.query(Usuario).filter_by(nombre_usuario=nombre_usuario).first()
    if usuario:
        receptor = input("¿A quién deseas agregar?: ")
        receptor_validado = sesion.query(Usuario).filter_by(nombre_usuario=receptor).first()
        if receptor_validado:
            enviar_solicitud(usuario.id_usuario, receptor_validado.id_usuario)
        else:
            print(f"Este usuario no se encuentra registrado en {nombre_aplicacion}")
    else:
        print("No estás registrado")

def aceptar_solicitud_amistad(id_emisor):
    responder_solicitud(id_emisor)