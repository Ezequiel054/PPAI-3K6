from sqlalchemy import (Column, Integer, String, DECIMAL)
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class TipoDeDato(Base):
    __tablename__ = "TipoDeDato"

    id = Column(Integer, primary_key=True, autoincrement=True)
    denominacion = Column(String(100), nullable=False)
    nombreUnidadMedida = Column(String(50))
    valorUmbral = Column(DECIMAL(10, 2))

    detalles = relationship("DetalleMuestraSismica", back_populates="tipoDeDato")

    def __repr__(self):
        return f"<TipoDeDato(denominacion='{self.denominacion}')>"
