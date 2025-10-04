from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text, CURRENT_TIMESTAMP
from modelos.base import BaseModel


class Comentario(BaseModel):
    id_comentario = Column(Integer, primary_key=True)
    comentario = Column(Text)
    id_publicacion = Column(Integer, ForeignKey('publicacion.id_publicacion'))
    id_usuario = Column(Integer, ForeignKey('usuario.id_usuario'))



        
    