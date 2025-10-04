from modelos.usuario import Usuario


class Amistad(Usuario):
    def __init__(self, id_primer_usuario, id_segundo_usuario, id_amistad, fecha_amistad):
        super().__init__(id_primer_usuario) # type: ignore
        super().__init__(id_segundo_usuario) # type: ignore
        id_amistad = id_amistad
        fecha_amistad = fecha_amistad



