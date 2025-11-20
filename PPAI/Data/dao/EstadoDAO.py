from Data.database import SessionLocal
from Data.models.Estado import EstadoModel

class EstadoDAO:
    def __init__(self, session=None):
        # si se pasa session externa, la usa (ideal para transacciones en EventoDAO)
        if session is not None:
            self.db = session
            self._owner = False
        else:
            self.db = SessionLocal()
            self._owner = True

    def find_by_nombre_y_ambito(self, nombreEstado, ambito):
        return self.db.query(EstadoModel).filter_by(nombreEstado=nombreEstado, ambito=ambito).first()

    def close(self):
        if self._owner:
            self.db.close()
