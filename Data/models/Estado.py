from sqlalchemy import (Column, Integer, String)
from sqlalchemy.orm import relationship
from Data.database import Base


class EstadoModel(Base):
    __tablename__ = "Estado"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ambito = Column(String(100))
    nombreEstado = Column(String(100))

    eventos = relationship("EventoSismicoModel", back_populates="estadoActual")
    cambios = relationship("CambioEstadoModel", back_populates="estado")

    def __repr__(self):
        return f"<Estado(nombre='{self.nombreEstado}')>"