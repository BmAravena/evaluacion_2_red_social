from datos.conexion import Session
from sqlalchemy.exc import SQLAlchemyError
from modelos.usuario import Usuario
from modelos.publicacion import Publicacion


sesion = Session()
    

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
        try:
            publi = input("Ingresa lo que deseas publicar: ")
            nueva_publicacion = Publicacion(contenido_publicacion=publi, id_usuario=usuario.id_usuario)
            sesion.add(nueva_publicacion)
            sesion.commit()
            print("Públicación creada exitosamente")

        except SQLAlchemyError as e:
            sesion.rollback()
            print(f"Error: {e}")
    else:
        print("Este usuario no existe, por favor intentálo nuevamente")

def realizar_comentario():
    pass


def enviar_solicitudamista():
    pass