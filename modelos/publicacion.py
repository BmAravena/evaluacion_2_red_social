from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text, DateTime, func
from modelos.base import BaseModel


class Publicacion(BaseModel):
    id_publicacion = Column(Integer, primary_key=True)
    contenido_publicacion = Column(Text)
    fecha_publicacion = Column(DateTime, server_default=func.now())
    id_usuario = Column(Integer, ForeignKey('usuario.id_usuario'))

