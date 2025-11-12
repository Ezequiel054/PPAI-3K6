from sqlalchemy import (Column, Integer, String)
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Estado(Base):
    __tablename__ = "Estado"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ambito = Column(String(100))
    nombreEstado = Column(String(100))

    eventos = relationship("EventoSismico", back_populates="estadoActual")
    cambios = relationship("CambioEstado", back_populates="estado")

    def __repr__(self):
        return f"<Estado(nombre='{self.nombreEstado}')>"