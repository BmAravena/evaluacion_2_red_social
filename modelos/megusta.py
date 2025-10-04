from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, func
from modelos.base import BaseModel


class Megusta(BaseModel):
    id_megusta = Column(Integer, primary_key=True)
    fecha_megusta = Column(DateTime, server_default=func.now())
    id_publicacion = Column(Integer, ForeignKey('publicacion.id_publicacion'))
    id_usuario = Column(Integer, ForeignKey('usuario.id_usuario'))

