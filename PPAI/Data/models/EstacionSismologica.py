from sqlalchemy import (Column, Integer, String, Date, DECIMAL)
from sqlalchemy.orm import relationship
from Data.database import Base


class EstacionSismologicaModel(Base):
    __tablename__ = "EstacionSismologica"

    id = Column(Integer, primary_key=True, autoincrement=True)
    codigoEstacion = Column(String(50), nullable=False)
    nombre = Column(String(100))
    latitud = Column(DECIMAL(10, 6))
    longitud = Column(DECIMAL(10, 6))
    nroCertificacionAdquisicion = Column(String(50))
    documentoCertificacionAdq = Column(String(255))
    fechaSolcitudCertificacion = Column(Date)

    sismografos = relationship("SismografoModel", back_populates="estacionSismologica")

    def __repr__(self):
        return f"<EstacionSismologica(codigo='{self.codigoEstacion}')>"

