from datos.conexion import Session
from sqlalchemy.exc import SQLAlchemyError


sesion = Session()

def registrar_usuario(nuevo_usuario):
    try:
        sesion.add(nuevo_usuario)
        sesion.commit()
        print("El usuario ha sido registrado exitosamente")
        
    except SQLAlchemyError as e:
        sesion.rollback()  # Revertir cambios si ocurre error
        print("Error al registrar el usuario:", e)
    

