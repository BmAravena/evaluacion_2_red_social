from sqlalchemy import Column, Integer, String, DateTime, func
from modelos.base import BaseModel


class Usuario(BaseModel):
    id_usuario = Column(Integer, primary_key=True)
    nombre_usuario = Column(String(155), nullable=False)
    contrasenha = Column(String(55), nullable=False)
    correo = Column(String(155), nullable=False)
    fecha_registro = Column(DateTime, server_default=func.now())



