from sqlalchemy import (Column, Integer, String, Text)
from sqlalchemy.orm import relationship
from Data.database import Base


class OrigenDeGeneracionModel(Base):
    __tablename__ = "OrigenDeGeneracion"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100))
    descripcion = Column(Text)

    eventos = relationship("EventoSismicoModel", back_populates="origenGeneracion")

    def __repr__(self):
        return f"<OrigenDeGeneracion(nombre='{self.nombre}')>"
