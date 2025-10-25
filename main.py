from iu.menu_principal import menu_principal
from datos.conexion import Session
from negocios.negocio_usuario import registrar_usuario, realizar_publicacion, realizar_comentario, enviar_solicitud_amistad, aceptar_solicitud_amistad, enviar_mensaje, ver_mensaje, dar_megusta, eliminar_amistad, editar_publicacion

from negocios.negocio_publicacion import visualizar_publicaciones


sesion = Session()

def app():
    verdadero = True
    while verdadero:
        print(f"\nBienvenido a")
        menu_principal()
        print()
        opcion = input("Ingrese opción[0-11]: ").strip()
        if opcion == '1':
            registrar_usuario()

        elif opcion == '2':
            realizar_publicacion()
    
        elif opcion == '3':
            realizar_comentario()

        elif opcion == '4':
            enviar_solicitud_amistad()

        elif opcion == '5':
            aceptar_solicitud_amistad()
            
        elif opcion == '6':
            eliminar_amistad()

        elif opcion == '7':
            enviar_mensaje()

        elif opcion == '8':
            ver_mensaje()
        
        elif opcion == '9':
            dar_megusta()
        
        elif opcion == '10':
            editar_publicacion()

        elif opcion == '11':
            visualizar_publicaciones()

        elif opcion == '0':
            print("saliendo del sistema...")
            verdadero = False


app()