from iu.menu_principal import menu_principal
from datos.conexion import Session
from negocios.negocio_usuario import registrar_usuario, realizar_publicacion, realizar_comentario, enviar_solicitudamistad


sesion = Session()

def app():
    verdadero = True
    while verdadero:
        print(f"\nBienvenido a")
        menu_principal()    
        print()
        opcion = input("Ingrese opción[0-7]: ")
        if opcion == '1':
            registrar_usuario()

        elif opcion == '2':
            realizar_publicacion()
    
        elif opcion == '3':
            realizar_comentario()

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