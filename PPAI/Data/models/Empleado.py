from sqlalchemy import (Column, Integer, String)
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Empleado(Base):
    __tablename__ = "Empleado"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100))
    apellido = Column(String(100))

    usuario = relationship("Usuario", back_populates="empleado", uselist=False)
    inspecciones = relationship("CambioEstado", back_populates="responsableInspeccion")

    def __repr__(self):
        return f"<Empleado(nombre='{self.nombre}', apellido='{self.apellido}')>"

