from sqlalchemy import (Column, Integer, ForeignKey, DECIMAL, DateTime)
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class EventoSismicoModel(Base):
    __tablename__ = "EventoSismico"

    id = Column(Integer, primary_key=True, autoincrement=True)
    fechaHoraOcurrencia = Column(DateTime)
    fechaHoraFin = Column(DateTime)
    latitudEpicentro = Column(DECIMAL(10, 6))
    latitudHipocentro = Column(DECIMAL(10, 6))
    longitudEpicentro = Column(DECIMAL(10, 6))
    longitudHipocentro = Column(DECIMAL(10, 6))
    valorMagnitud = Column(DECIMAL(4, 2))

    origenGeneracion_id = Column(Integer, ForeignKey("OrigenDeGeneracion.id"))
    alcanceSismo_id = Column(Integer, ForeignKey("AlcanceSismo.id"))
    estadoActual_id = Column(Integer, ForeignKey("Estado.id"))

    clasificacionSismo = relationship("ClasificacionSismoModel", back_populates="eventos")
    origenGeneracion = relationship("OrigenDeGeneracion", back_populates="eventos")
    alcanceSismo = relationship("AlcanceSismo", back_populates="eventos")
    estadoActual = relationship("Estado", back_populates="eventos")
    series = relationship("SerieTemporal", back_populates="eventoSismico", cascade="all, delete-orphan")
    cambiosEstado = relationship("CambioEstado", back_populates="eventoSismico", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<EventoSismico(id={self.id}, magnitud={self.valorMagnitud})>"

