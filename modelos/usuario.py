from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, CURRENT_TIMESTAMP
from modelos.base import BaseModel


class Usuario(BaseModel):
    id_usuario = Column(Integer, primary_key=True)
    nombre_usuario = Column(String(155))
    contrasenha = Column(String(55))
    correo = Column(String(155))
    fecha_registro = Column(DateTime, CURRENT_TIMESTAMP)



