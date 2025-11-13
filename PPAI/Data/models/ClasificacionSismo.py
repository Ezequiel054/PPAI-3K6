from sqlalchemy import (Column, Integer, DECIMAL, String)
from sqlalchemy.orm import relationship
from Data.database import Base


class ClasificacionSismoModel(Base):
    __tablename__ = "ClasificacionSismo"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50))
    kmProfundidadDesde = Column(DECIMAL)
    kmProfundidadHasta = Column(DECIMAL)

    eventos = relationship("EventoSismicoModel", back_populates="clasificacionSismo")

    def __repr__(self):
        return f"<ClasificacionSismo(id={self.id})>"
