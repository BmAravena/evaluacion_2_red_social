from modelos.megusta import Me_gusta
from datos.obtener_datos import obtener_datos


# Función para validar me gusta, primero obtenemos una lista de todos los me gusta
def valida_megusta(pub, usu):
    megustas = obtener_datos(Me_gusta)
    # Iteramos la lista y validamos si la id de la publicación del me gusta es igual a la id de la publicación que se obtiene como parámetro
    for megusta in megustas: 
        if (megusta.id_publicacion == pub.id_publicacion and megusta.id_usuario == usu.id_usuario):
            return True
        
    return False