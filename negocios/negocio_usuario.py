from datos.conexion import Session
from sqlalchemy.exc import SQLAlchemyError
from modelos.usuario import Usuario
from modelos.publicacion import Publicacion
from modelos.megusta import Me_gusta
from negocios.negocio_publicacion import valida_publicacion, visualizar_publicaciones
from negocios.negocio_comentario import valida_comentario
from negocios.negocio_amistad import enviar_solicitud, responder_solicitud, valida_amistad
from auxiliares.info_app import nombre_aplicacion
from datos.obtener_datos import obtener_datos
from negocios.negocio_mensaje import valida_envia_mensaje, visualizar_mensajes



sesion = Session()
    

def validador_de_identidad():
    nombre_usuario = input("Ingresa tu nombre de usuario: ")
    usuario = obtener_datos(Usuario)
    return usuario


def buscar_usuario(info_usuario):
    usuarios = obtener_datos(Usuario) # Lista
    usuario = Usuario # Emisor
    for user in usuarios:
        if user.nombre_usuario == info_usuario:
            usuario = user
            return usuario
        elif user.correo == info_usuario:
            usuario = user
            return usuario


def registrar_usuario():
    nombre_usuario_registro = input("Ingresa nombre de usuario: ")
    usuario = buscar_usuario(nombre_usuario_registro)

    if not usuario:
        correo_usuario_registro = input("Ingresa el correo: ")
        mail = buscar_usuario(correo_usuario_registro)

        if not mail:
            contrasenha = input("Ingresa una contraseña: ")
            nuevo_usuario = Usuario(nombre_usuario=nombre_usuario_registro, contrasenha=contrasenha, correo=correo_usuario_registro)
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
    usuario = buscar_usuario(nombre_usuario)

    if usuario:
        valida_publicacion(usuario)
    else:
        print("Este usuario no existe, por favor intentálo nuevamente")




def realizar_comentario():
    nombre_usuario = input("Ingresa tu nombre de usuario: ")

    usuarios = obtener_datos(Usuario) # Lista
    usuario = Usuario # Emisor
    for user in usuarios:
        if user.nombre_usuario == nombre_usuario:
            usuario = user

    if usuario:
        publicaciones = obtener_datos(Publicacion)
        publicacion = Publicacion
        id_publi = int(input("Ingresa la ID de la públicación a comentar: "))
        for pub in publicaciones:
            if pub.id_publicacion == id_publi:
                publicacion = pub

        if publicacion:
            valida_comentario(publicacion, usuario)
        else: 
            print("Esa públicación no existe, intentálo nuevamente")
    else:
        print("Este usuario no existe, por favor intentálo nuevamente")




def enviar_solicitud_amistad():
    buscar_usuario = input("Ingresa tu nombre de usuario: ")

    usuarios = obtener_datos(Usuario) # Lista
    usuario_e = Usuario # Emisor
    for user in usuarios:
        if user.nombre_usuario == buscar_usuario:
            usuario_e = user
            
    if usuario_e:
        receptor = input("¿A quién deseas agregar?: ")
        usuario_r = Usuario # Receptor
        for user in usuarios:
            if user.nombre_usuario == receptor:
                usuario_r = user

        if usuario_r:
            enviar_solicitud(usuario_e.id_usuario, usuario_r.id_usuario)
            return usuario_r
        
        else:
            print(f"Este usuario no se encuentra registrado en {nombre_aplicacion}")
    else:
        print("No estás registrado")


def aceptar_solicitud_amistad():
    buscar_usuario = input("Ingresa tu nombre de usuario: ")
    usuarios = obtener_datos(Usuario) # Lista
    for user in usuarios:
        if user.nombre_usuario == buscar_usuario:
            usuario = user

    if usuario:
        responder_solicitud(usuario.id_usuario)
    else:
        print("Este usuario no existe, por favor intentálo nuevamente")


def enviar_mensaje():
    nombre_usuario_emisor = input("Ingresa tu nombre de usuario: ")
    usuario_e = buscar_usuario(nombre_usuario_emisor)
    if usuario_e:
        nombre_usuario_receptor = input("¿A quién deseas enviar un mensaje(dentro de tus amigos)?: ")
        usuario_r = buscar_usuario(nombre_usuario_receptor)
        amistad_validada = valida_amistad(usuario_e, usuario_r)
        if amistad_validada:
            valida_envia_mensaje(usuario_e, usuario_r)
        else:
            print(f"No es posible enviar un mensaje a {nombre_usuario_receptor}, porque no son amigos ")


def ver_mensaje():
    nombre_usuario = input("Ingresa tu nombre de usuario: ")
    usuario = buscar_usuario(nombre_usuario)
    if usuario:
        visualizar_mensajes(usuario.id_usuario)



def dar_megusta():
    nombre_usuario = input("Ingresa tu nombre de usuario: ")
    usuario = buscar_usuario(nombre_usuario)
    id_usuario = usuario.id_usuario

    if usuario:
        visualizar_publicaciones()
        opcion = int(input("¿A que públicación deseas darle me gusta(ID)?: "))
        publicaciones = obtener_datos(Publicacion)
        for pub in publicaciones:
            if pub.id_publicacion == opcion:
                megusta = Me_gusta(id_publicacion=opcion, id_usuario=id_usuario)
                print(f"Haz dado me gusta a {pub.contenido_publicacion} correctamente...")

        sesion.add(megusta)
        sesion.commit()


