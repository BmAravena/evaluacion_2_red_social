from auxiliares.info_app import nombre_aplicacion
from auxiliares.version import numero_version

def menu_principal():
    print(f"Nombre: {nombre_aplicacion} Versión: {numero_version}")
    print("="*51)
    print("[1] Registrar usuario")
    print("[2] Realizar publicación")
    print("[3] Realizar comentario")
    print("[4] Enviar solicitud")
    print("[5] Aceptar solicitud")
    print("[6] Enviar mensaje")
    print("[7] Ver mensaje")
    print("[8] Dar me gusta")
    print("[0] Salir del sistema")