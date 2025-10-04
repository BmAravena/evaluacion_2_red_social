from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text, CURRENT_TIMESTAMP
from modelos.base import BaseModel


class Mensaje(BaseModel):
    id_mensaje = Column(Integer, primary_key=True)
    contenido_mensaje = Column(Text)
    fecha_mensaje = Column(DateTime=CURRENT_TIMESTAMP)
    id_primer_usuario = Column(Integer, ForeignKey('usuario.id_usuario'))
    id_segundo_usuario = Column(Integer, ForeignKey('usuario.id_usuario'))


