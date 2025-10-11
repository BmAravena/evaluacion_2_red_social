from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, func
from modelos.base import BaseModel


class Amistad(BaseModel):
    id_amistad = Column(Integer, primary_key=True)
    estado = Column(String(25), default="pendiente", nullable=False)
    fecha_amistad = Column(DateTime, server_default=func.now())
    id_primer_usuario = Column(Integer, ForeignKey('usuario.id_usuario'))
    id_segundo_usuario = Column(Integer, ForeignKey('usuario.id_usuario'))





