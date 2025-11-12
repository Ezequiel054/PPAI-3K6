from sqlalchemy import (Column, Integer, DECIMAL)
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class ClasificacionSismoModel(Base):
    __tablename__ = "ClasificacionSismo"

    id = Column(Integer, primary_key=True, autoincrement=True)
    kmProfundidadDesde = Column(DECIMAL)
    kmProfundidadHasta = Column(DECIMAL)

    eventos = relationship("EventoSismico", back_populates="clasificacionSismo")

    def __repr__(self):
        return f"<ClasificacionSismo(id={self.id})>"