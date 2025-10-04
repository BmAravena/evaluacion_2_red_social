from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text, CURRENT_TIMESTAMP
from modelos.base import BaseModel


class Publicacion(BaseModel):
    id_publicacion = Column(Integer, primary_key=True)
    contenido_publicacion = Column(Text)
    fecha_publicacion = Column(DateTime=CURRENT_TIMESTAMP)
    id_usuario = Column(Integer, ForeignKey('usuario.id_usuario'))

