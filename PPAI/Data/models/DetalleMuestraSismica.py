from sqlalchemy import (Column, Integer, DECIMAL, ForeignKey)
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class DetalleMuestraSismica(Base):
    __tablename__ = "DetalleMuestraSismica"

    id = Column(Integer, primary_key=True, autoincrement=True)
    valor = Column(DECIMAL(10, 4))
    tipoDeDato_id = Column(Integer, ForeignKey("TipoDeDato.id"))
    muestraSismica_id = Column(Integer, ForeignKey("MuestraSismica.id"))

    tipoDeDato = relationship("TipoDeDato", back_populates="detalles")
    muestraSismica = relationship("MuestraSismica", back_populates="detalles")

    def __repr__(self):
        return f"<DetalleMuestraSismica(id={self.id}, valor={self.valor})>"

