from sqlalchemy import (Column, Integer, String, Text)
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class AlcanceSismo(Base):
    __tablename__ = "AlcanceSismo"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text)

    eventos = relationship("EventoSismico", back_populates="alcanceSismo")

    def __repr__(self):
        return f"<AlcanceSismo(nombre='{self.nombre}')>"
