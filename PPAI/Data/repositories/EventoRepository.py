from Data.dao.baseDao import BaseDAO
from Data.models.EventoSismico import EventoSismicoModel
from Data.models.Estado import EstadoModel
from Data.database import SessionLocal

class EventoRepository:
    @staticmethod
    def find_evento_id(evento):
        """
        Intenta retornar el id del EventoSismico en BD a partir de la entidad.
        """
        if hasattr(evento, "get_db_id") and evento.get_db_id():
            return evento.get_db_id()
        session = SessionLocal()
        row = session.query(EventoSismicoModel).filter_by(
            fechaHoraOcurrencia=getattr(evento, "fechaHoraOcurrencia", None),
            valorMagnitud=getattr(evento, "valorMagnitud", None)
        ).first()
        session.close()
        return row.id if row else None

    @staticmethod
    def update_estado(evento, estado_entity):
        evento_id = EventoRepository.find_evento_id(evento)
        if not evento_id:
            return False
        # resolver id del estado buscando por nombre/ambito
        session = SessionLocal()
        estado_row = session.query(EstadoModel).filter_by(
            nombreEstado=getattr(estado_entity, "nombreEstado", None),
            ambito=getattr(estado_entity, "ambito", None)
        ).first()
        session.close()
        if not estado_row:
            return False
        dao = BaseDAO(EventoSismicoModel)
        dao.update_field(evento_id, 'estadoActual_id', estado_row.id)
        dao.close()
        return True
