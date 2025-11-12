from sqlalchemy import (Column, Integer, DateTime, ForeignKey)
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class MuestraSismica(Base):
    __tablename__ = "MuestraSismica"

    id = Column(Integer, primary_key=True, autoincrement=True)
    fechaHoraMuestra = Column(DateTime, nullable=False)
    serieTemporal_id = Column(Integer, ForeignKey("SerieTemporal.id"))

    serieTemporal = relationship("SerieTemporal", back_populates="muestras")
    detalles = relationship("DetalleMuestraSismica", back_populates="muestraSismica", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<MuestraSismica(id={self.id}, fecha={self.fechaHoraMuestra})>"
    