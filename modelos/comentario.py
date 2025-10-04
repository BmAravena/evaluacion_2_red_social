from modelos.publicacion import Publicacion
from modelos.usuario import Usuario

class Comentario(Publicacion, Usuario):
    def __init__(self, id_publicacion, id_usuario, id_comentario, comentario):
        super().__init__(id_publicacion) # type: ignore
        super().__init__(id_usuario) # type: ignore
        self.id_comentario = id_comentario
        self.id_comentario = comentario
        
    