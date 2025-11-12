from sqlalchemy import (Column, Integer, String, ForeignKey)
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "Usuario"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombreUsuario = Column(String(100), nullable=False)
    password = Column(String(255), nullable=False)
    empleado_id = Column(Integer, ForeignKey("Empleado.id"))

    empleado = relationship("Empleado", back_populates="usuario")
    sesiones = relationship("Sesion", back_populates="usuario", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Usuario(nombreUsuario='{self.nombreUsuario}')>"
