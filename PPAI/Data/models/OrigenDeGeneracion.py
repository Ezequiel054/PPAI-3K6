from sqlalchemy import (Column, Integer, String, Text)
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class OrigenDeGeneracion(Base):
    __tablename__ = "OrigenDeGeneracion"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100))
    descripcion = Column(Text)

    eventos = relationship("EventoSismico", back_populates="origenGeneracion")

    def __repr__(self):
        return f"<OrigenDeGeneracion(nombre='{self.nombre}')>"
