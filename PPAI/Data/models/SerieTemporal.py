from sqlalchemy import (Column, Integer, Boolean, ForeignKey, DateTime, DECIMAL)
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class SerieTemporal(Base):
    __tablename__ = "SerieTemporal"

    id = Column(Integer, primary_key=True, autoincrement=True)
    condicionAlarma = Column(Boolean)
    fechaHoraInicioRegistroMuestras = Column(DateTime)
    fechaHoraRegistro = Column(DateTime)
    frecuenciaMuestreo = Column(DECIMAL(10, 2))

    eventoSismico_id = Column(Integer, ForeignKey("EventoSismico.id"))

    eventoSismico = relationship("EventoSismico", back_populates="series")
    muestras = relationship("MuestraSismica", back_populates="serieTemporal", cascade="all, delete-orphan")
    sismografo = relationship("Sismografo", back_populates="serieTemporal", uselist=False)

    def __repr__(self):
        return f"<SerieTemporal(id={self.id}, frecuencia={self.frecuenciaMuestreo})>"
