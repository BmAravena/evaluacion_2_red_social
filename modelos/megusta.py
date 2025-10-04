from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, CURRENT_TIMESTAMP
from modelos.base import BaseModel


class Megusta(BaseModel):
    id_megusta = Column(Integer, primary_key=True)
    fecha_megusta = Column(DateTime=CURRENT_TIMESTAMP)
    id_publicacion = Column(Integer, ForeignKey('publicacion.id_publicacion'))
    id_usuario = Column(Integer, ForeignKey('usuario.id_usuario'))

