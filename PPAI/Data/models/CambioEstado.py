from sqlalchemy import (Column, Integer, DateTime, ForeignKey)
from sqlalchemy.orm import relationship
from Data.database import Base


class CambioEstadoModel(Base):
    __tablename__ = "CambioEstado"

    id = Column(Integer, primary_key=True, autoincrement=True)
    fechaHoraInicio = Column(DateTime)
    fechaHoraFin = Column(DateTime)
    estado_id = Column(Integer, ForeignKey("Estado.id"))
    responsableInspeccion_id = Column(Integer, ForeignKey("Empleado.id"))
    eventoSismico_id = Column(Integer, ForeignKey("EventoSismico.id"))

    estado = relationship("EstadoModel", back_populates="cambios")
    responsableInspeccion = relationship("EmpleadoModel", back_populates="inspecciones")
    eventoSismico = relationship("EventoSismicoModel", back_populates="cambiosEstado")

    def __repr__(self):
        return f"<CambioEstado(id={self.id}, estado_id={self.estado_id})>"
