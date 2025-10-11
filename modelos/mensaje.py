from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text, DateTime, func
from modelos.base import BaseModel


class Mensaje(BaseModel):
    id_mensaje = Column(Integer, primary_key=True)
    contenido_mensaje = Column(Text, nullable=False)
    fecha_mensaje = Column(DateTime, server_default=func.now())
    id_primer_usuario = Column(Integer, ForeignKey('usuario.id_usuario'))
    id_segundo_usuario = Column(Integer, ForeignKey('usuario.id_usuario'))


