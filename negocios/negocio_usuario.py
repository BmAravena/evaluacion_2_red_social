from datos.conexion import Session
from sqlalchemy.exc import SQLAlchemyError
from modelos.usuario import Usuario


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
