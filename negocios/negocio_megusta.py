from modelos.megusta import Me_gusta
from datos.obtener_datos import obtener_datos



def valida_megusta(pub, usu):
    megustas = obtener_datos(Me_gusta)
    for megusta in megustas: 
        if (megusta.id_publicacion == pub.id_publicacion and megusta.id_usuario == usu.id_usuario):
            return True
        
    return False