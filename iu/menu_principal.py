from auxiliares.info_app import nombre_aplicacion
from auxiliares.version import numero_version

def menu_principal():
    print("="*51)
    print(f"Nombre: {nombre_aplicacion} Versión: {numero_version}")
    print("="*51)
    print("[1] Registrar usuario")
    print("[2] Realizar publicación")
    print("[3] Realizar comentario")
    print("[4] Enviar solicitud")
    print("[5] Aceptar solicitud")
    print("[6] Eliminar amistad")
    print("[7] Enviar mensaje")
    print("[8] Ver mensaje")
    print("[9] Dar me gusta")
    print("[10] Visualizar publicaciones")
    print("[0] Salir del sistema")