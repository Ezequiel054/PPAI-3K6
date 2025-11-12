from sqlalchemy import (Column, Integer, DateTime, ForeignKey)
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Sesion(Base):
    __tablename__ = "Sesion"

    id = Column(Integer, primary_key=True, autoincrement=True)
    fechaHoraDesde = Column(DateTime)
    fechaHoraHasta = Column(DateTime)
    usuario_id = Column(Integer, ForeignKey("Usuario.id"))

    usuario = relationship("Usuario", back_populates="sesiones")

    def __repr__(self):
        return f"<Sesion(id={self.id}, usuario_id={self.usuario_id})>"