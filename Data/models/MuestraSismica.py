from sqlalchemy import (Column, Integer, DateTime, ForeignKey)
from sqlalchemy.orm import relationship
from Data.database import Base


class MuestraSismicaModel(Base):
    __tablename__ = "MuestraSismica"

    id = Column(Integer, primary_key=True, autoincrement=True)
    fechaHoraMuestra = Column(DateTime, nullable=False)
    serieTemporal_id = Column(Integer, ForeignKey("SerieTemporal.id"))

    serieTemporal = relationship("SerieTemporalModel", back_populates="muestras")
    detalles = relationship("DetalleMuestraSismicaModel", back_populates="muestraSismica", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<MuestraSismica(id={self.id}, fecha={self.fechaHoraMuestra})>"
    