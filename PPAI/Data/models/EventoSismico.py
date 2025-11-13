from sqlalchemy import (Column, Integer, ForeignKey, DECIMAL, DateTime)
from sqlalchemy.orm import relationship
from Data.database import Base


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

    clasificacionSismo_id = Column(Integer, ForeignKey("ClasificacionSismo.id"))
    origenGeneracion_id = Column(Integer, ForeignKey("OrigenDeGeneracion.id"))
    alcanceSismo_id = Column(Integer, ForeignKey("AlcanceSismo.id"))
    estadoActual_id = Column(Integer, ForeignKey("Estado.id"))

    clasificacionSismo = relationship("ClasificacionSismoModel", back_populates="eventos")
    origenGeneracion = relationship("OrigenDeGeneracionModel", back_populates="eventos")
    alcanceSismo = relationship("AlcanceSismoModel", back_populates="eventos")
    estadoActual = relationship("EstadoModel", back_populates="eventos")
    series = relationship("SerieTemporalModel", back_populates="eventoSismico", cascade="all, delete-orphan")
    cambiosEstado = relationship("CambioEstadoModel", back_populates="eventoSismico", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<EventoSismico(id={self.id}, magnitud={self.valorMagnitud})>"

