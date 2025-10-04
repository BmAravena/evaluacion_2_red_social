from iu.menu_principal import menu_principal
from datos.conexion import Session
from modelos.usuario import Usuario
from negocios.negocio_usuario import registrar_usuario


sesion = Session()

def app():
    verdadero = True
    while verdadero:
        print(f"\nBienvenido a")
        menu_principal()    
        print()
        opcion = input("Ingrese opción[0-7]: ")
        if opcion == '1':
            usuario = input("Ingresa nombre de usuario: ")
            existe_usuario = sesion.query(Usuario).filter_by(nombre_usuario=usuario).first()
            if not existe_usuario:
                mail = input("Ingresa el correo: ")
                existe_correo = sesion.query(Usuario).filter_by(correo=mail).first()
                if not existe_correo:
                    contrasenha = input("Ingresa una contraseña: ")
                    nuevo_usuario = Usuario(nombre_usuario=usuario, contrasenha=contrasenha, correo=mail)
                    registrar_usuario(nuevo_usuario)
                else:
                    print("Este correo ya está registrado, por favor intentálo nuevamente")
            else:
                print("Este nombre de usuario ya está registrado, por favor intentálo nuevamente")

        elif opcion == '2':
            pass
        elif opcion == '3':
            pass
        elif opcion == '4':
            pass
        elif opcion == '5':
            pass
        elif opcion == '6':
            pass
        elif opcion == '7':
            pass
        elif opcion == '0':
            print("saliendo del sistema...")
            verdadero = False


app()