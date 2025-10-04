from modelos.usuario import Usuario

class Publicacion(Usuario):
    def __init__(self, id_usuario, id_publicacion, contenido_publicacion, fecha_publicacion):
        super().__init__(id_usuario) # type: ignore
        self.id_publicacion = id_publicacion
        self.contenido_publicacion = contenido_publicacion
        self.fecha_publicacion = fecha_publicacion