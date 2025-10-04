from modelos.usuario import Usuario

class Mensaje(Usuario):
    def __init__(self, id_primer_usuario, id_segundo_usuario, id_mensaje, contenido_mensaje, fecha_mensaje):
        super().__init__(id_primer_usuario) # type: ignore
        super().__init__(id_segundo_usuario) # type: ignore
        self.id_mensaje = id_mensaje
        self.contenido_mensaje = contenido_mensaje
        self.fecha_mensaje = fecha_mensaje
