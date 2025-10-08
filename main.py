from iu.menu_principal import menu_principal
from datos.conexion import Session
from negocios.negocio_usuario import registrar_usuario, realizar_publicacion, realizar_comentario, enviar_solicitud_amistad, aceptar_solicitud_amistad, enviar_mensaje
from negocios.negocio_amistad import responder_solicitud

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
            #solicitud = enviar_solicitud_amistad()
            enviar_solicitud_amistad()

        elif opcion == '5':
            #responder_solicitud(solicitud)
            aceptar_solicitud_amistad()
            
        elif opcion == '6':
            enviar_mensaje()

        elif opcion == '7':
            pass

        elif opcion == '8':
            pass

        elif opcion == '0':
            print("saliendo del sistema...")
            verdadero = False


app()