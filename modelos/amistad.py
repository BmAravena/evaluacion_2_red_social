from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, CURRENT_TIMESTAMP
from modelos.base import BaseModel


class Amistad(BaseModel):
    id_amistad = Column(Integer, primary_key=True)
    fecha_amistad = Column(DateTime=CURRENT_TIMESTAMP)
    id_primer_usuario = Column(Integer, ForeignKey('usuario.id_usuario'))
    id_segundo_usuario = Column(Integer, ForeignKey('usuario.id_usuario'))





