from modelos.publicacion import Publicacion
from modelos.usuario import Usuario

class Megusta(Publicacion, Usuario):
    def __init__(self, id_publicacion, id_usuario, id_megusta, fecha_megusta):
        super().__init__(id_publicacion) # type: ignore
        super().__init__(id_usuario) # type: ignore
        self.id_megusta = id_megusta
        self.fecha_megusta = fecha_megusta