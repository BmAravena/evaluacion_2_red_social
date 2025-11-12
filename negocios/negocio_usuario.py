from datos.conexion import sesion
from sqlalchemy.exc import SQLAlchemyError
from modelos.usuario import Usuario
from modelos.publicacion import Publicacion
from modelos.megusta import Me_gusta
from modelos.amistad import Amistad
from negocios.negocio_publicacion import valida_publicacion, visualizar_publicaciones
from negocios.negocio_comentario import valida_comentario
from negocios.negocio_amistad import enviar_solicitud, responder_solicitud, valida_amistad
from auxiliares.info_app import nombre_aplicacion
from datos.obtener_datos import obtener_datos
from negocios.negocio_mensaje import valida_envia_mensaje, visualizar_mensajes
from negocios.negocio_megusta import valida_megusta


    

def validador_de_identidad():
    nombre_usuario = input("Ingresa tu nombre de usuario: ")
    usuario = obtener_datos(Usuario)
    return usuario

# Buscamos un usuario recibiendo su nombre o correo, dependiendo del caso
def buscar_usuario(info_usuario):
    usuarios = obtener_datos(Usuario) # Lista
    #usuario = Usuario # Emisor
    usuario = None
    for user in usuarios:
        if user.nombre_usuario == info_usuario:
            usuario = user
            return usuario
        elif user.correo == info_usuario:
            usuario = user
            return usuario


# Registramos un usuario verificando por cada atributo que no se repita información dentro de la base de datos
def registrar_usuario():
    nombre_usuario_registro = input("Ingresa nombre de usuario: ")
    # Hacemos la previa validación de si existe o no
    usuario = buscar_usuario(nombre_usuario_registro)

    if not usuario:
        correo_usuario_registro = input("Ingresa el correo: ")
        mail = buscar_usuario(correo_usuario_registro)

        if not mail:
            contrasenha = input("Ingresa una contraseña: ")
            # Instanciamos un nuevo usuario con los datos anterior que ya hemos verificado
            nuevo_usuario = Usuario(nombre_usuario=nombre_usuario_registro, contrasenha=contrasenha, correo=correo_usuario_registro)
            try:
                # Y lo agregamos a la base de datos
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


# Realizamos una publicación, acá únicamente recibimos el usuario, verificamos que existe, y si existe vamos a la función secundaria valida_publicación la cual se encargará de agregar
def realizar_publicacion():
    nombre_usuario = input("Ingresa tu nombre de usuario: ")
    usuario = buscar_usuario(nombre_usuario)

    if usuario:
        valida_publicacion(usuario)
    else:
        print("Este usuario no existe, por favor intentálo nuevamente")



# Realizamos un comentario
def realizar_comentario():
    nombre_usuario = input("Ingresa tu nombre de usuario: ")
    # Iteramos los usuarios existentes en la base de datos
    usuarios = obtener_datos(Usuario) # Lista
    usuario = Usuario # Emisor
    for user in usuarios:
        if user.nombre_usuario == nombre_usuario:
            usuario = user

    # Si encontramos el usuario
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
    # Si no
    else:
        print("Este usuario no existe, por favor intentálo nuevamente")



# Enviamos una solicitud de amistad, validando previamente que nuestro usuario existe en el sistema
def enviar_solicitud_amistad():
    buscar_usuario = input("Ingresa tu nombre de usuario: ")

    usuarios = obtener_datos(Usuario) # Lista
    usuario_e = Usuario # Emisor
    for user in usuarios:
        if user.nombre_usuario == buscar_usuario:
            usuario_e = user
    # Si existe nuestro usuario, pedimos el nombre de la persona a agregar       
    if usuario_e:
        receptor = input("¿A quién deseas agregar?: ")
        usuario_r = Usuario # Receptor
        for user in usuarios:
            if user.nombre_usuario == receptor:
                usuario_r = user

        # Obtenemos los datos del usuario receptor,
        # en caso de encontrarlo enviamos tanto el usuario emisor y receptor a nuestra función enviar_solicitud 
        if usuario_r:
            enviar_solicitud(usuario_e, usuario_r)
            #enviar_solicitud(usuario_e.id_usuario, usuario_r.id_usuario)
            return usuario_r
        
        else:
            print(f"Este usuario no se encuentra registrado en {nombre_aplicacion}")
    else:
        print("No estás registrado")

# Aceptamos solicitud, verificamos que nuestro usuario existe en el sistema
def aceptar_solicitud_amistad():
    buscar_usuario = input("Ingresa tu nombre de usuario: ")
    usuarios = obtener_datos(Usuario) # Lista
    for user in usuarios:
        if user.nombre_usuario == buscar_usuario:
            usuario = user
    # Si existe enviamos nuestra id a la función para responder solicitud
    if usuario:
        responder_solicitud(usuario.id_usuario)
    else:
        print("Este usuario no existe, por favor intentálo nuevamente")

# Enviamos mensajes, verificamos que nuestro usuario existe en el sistema
def enviar_mensaje():
    nombre_usuario_emisor = input("Ingresa tu nombre de usuario: ")
    usuario_e = buscar_usuario(nombre_usuario_emisor)
    # Si existe nuestro usuario, pedimos información del usuario a agregar
    if usuario_e:
        nombre_usuario_receptor = input("¿A quién deseas enviar un mensaje(dentro de tus amigos)?: ")
        # Obtenemos el usuario receptor
        usuario_r = buscar_usuario(nombre_usuario_receptor)
        # Validamos que exista una amistad entre usuarios, para poder enviar un mensaje
        amistad_validada = valida_amistad(usuario_e, usuario_r)
        if amistad_validada:
            valida_envia_mensaje(usuario_e, usuario_r)
        else:
            print(f"No es posible enviar un mensaje a {nombre_usuario_receptor}, porque no son amigos ")

# Ver mensajes, si existe nuestro usuario hacemos llamada de la función visualizar_mensajes y le pasamos nuestra Id
def ver_mensaje():
    nombre_usuario = input("Ingresa tu nombre de usuario: ")
    usuario = buscar_usuario(nombre_usuario)
    if usuario:
        visualizar_mensajes(usuario.id_usuario)


# Dar megusta, verificamos que existe nuestro usuario
def dar_megusta():
    nombre_usuario = input("Ingresa tu nombre de usuario: ")
    usuario = buscar_usuario(nombre_usuario)
    id_usuario = usuario.id_usuario
    # Si existe, obtenemos visualmente las publicaciones con posibilidad de dar me gusta
    if usuario:
        visualizar_publicaciones()
        # Verificamos a qué publicación se desea dar me gusta mediante la Id de una de estas publicaciones
        opcion = int(input("¿A que públicación deseas darle me gusta(ID)?: "))
        # Obtenemos las publicaciones
        publicaciones = obtener_datos(Publicacion)
        # Iteramos las publicaciones
        for pub in publicaciones:
            if pub.id_publicacion == opcion:
                if (valida_amistad(usuario, pub)):
                    if not(valida_megusta(pub, usuario)):
                        megusta = Me_gusta(id_publicacion=opcion, id_usuario=id_usuario)
                        sesion.add(megusta)
                        sesion.commit()
                        print(f"Haz dado me gusta a {pub.contenido_publicacion} correctamente...")
                    else:
                        print("Ya le diste me gusta a esta publicación")
                else:
                    print("No puedes darle me gusta a la publicación, porque no eres amigo de la persona que la publicó")

         
# Eliminamos una amistad, validamos si existe nuestro usuario
def eliminar_amistad():
    nombre_usuario = input("Ingresa tu nombre de usuario: ")
    usuario = buscar_usuario(nombre_usuario)
    id_usuario = usuario.id_usuario
    # Obtenemos las amistades e iteramos sobre ellas
    amistad = Amistad
    amistades = obtener_datos(amistad)
    for amis in amistades:
        if amis.id_primer_usuario == id_usuario or amis.id_segundo_usuario == id_usuario:
            # Obtenemos nombre del usuario a eliminar
            nombre_usuario_a_eliminar = input("Ingresa el nombre del usuario que deseas eliminar: ")
            # Lo obtenemos
            usuario_eliminar = buscar_usuario(nombre_usuario_a_eliminar)
            # Si existe usamos nuestra función valida_amistad la cual nos retornará True-False y una amistad
            if usuario_eliminar:
                amistad_encontrada, amistad_a_borrar = valida_amistad(usuario, usuario_eliminar)

                if amistad_encontrada:
                    #sesion.delete(sesion.merge(amistad_a_borrar))
                    sesion.delete(amistad_a_borrar)
                    sesion.commit()
                    print(f"Amistad con {nombre_usuario_a_eliminar} eliminada correctamente")
                    break
                else:
                    print(f"No eres amigo de {nombre_usuario_a_eliminar}")
                
# Editamos publicación, primero validamos si existe el usuario que desea hacer la operación
def editar_publicacion():
    nombre_usuario = input("Ingresa tu nombre de usuario: ")
    usuario = buscar_usuario(nombre_usuario)
    # Si no existe se acaba la función
    if not usuario:
        print("Usuario no encontrado.")
        return

    id_usuario = usuario.id_usuario
    # Le pedimos la publicación a editar
    id_publicacion_editar = int(input("Ingresa la id de la publicación que deseas editar: "))
    # Obtenemos las publicaciones
    publicaciones = obtener_datos(Publicacion)
    publicacion_encontrada = None
    una_pub = publicaciones[0]
    #print(una_pub.__dict__)
    # Buscar la publicación según su id
    for pub in publicaciones:
        if pub.id_publicacion == id_publicacion_editar:
            publicacion_encontrada = pub
            break

    # Validar si existe
    if not publicacion_encontrada:
        print(f"Error: la publicación con la id {id_publicacion_editar} no existe.")
        return

    # Validar si pertenece al usuario
    if publicacion_encontrada.id_usuario != id_usuario:
        print("Error: esta publicación no te pertenece.")
        return

    # Editar publicación
    nuevo_contenido = input("Ingresa el nuevo contenido de la publicación: ")
    publicacion_encontrada.contenido_publicacion = nuevo_contenido
    sesion.commit()
    print("Publicación editada correctamente.")
        

