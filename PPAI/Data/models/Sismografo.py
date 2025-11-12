from sqlalchemy import (Column, Integer, String, Date, ForeignKey)
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Sismografo(Base):
    __tablename__ = "Sismografo"

    id = Column(Integer, primary_key=True, autoincrement=True)
    fechaAdquisicion = Column(Date)
    identificadorSismografo = Column(String(50), nullable=False)
    nroSerie = Column(String(50))
    estacionSismologica_id = Column(Integer, ForeignKey("EstacionSismologica.id"))
    serieTemporal_id = Column(Integer, ForeignKey("SerieTemporal.id"))

    estacionSismologica = relationship("EstacionSismologica", back_populates="sismografos")
    serieTemporal = relationship("SerieTemporal", back_populates="sismografo")

    def __repr__(self):
        return f"<Sismografo(identificador='{self.identificadorSismografo}')>"
