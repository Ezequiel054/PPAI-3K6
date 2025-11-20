from Data.dao.baseDao import BaseDAO
from Data.models.CambioEstado import CambioEstadoModel
from Data.models.Estado import EstadoModel
from Data.models.Empleado import EmpleadoModel
from Data.models.EventoSismico import EventoSismicoModel
from Data.mappers.CambioDeEstadoMapper import cambio_to_model
from Data.database import SessionLocal

class CambioEstadoRepository:
    @staticmethod
    def persist_closed_changes(evento):
        """
        Persiste fechaHoraFin de cambios cerrados en memoria.
        """
        dao = BaseDAO(CambioEstadoModel)
        session = dao.db
        for cambio in evento.cambiosEstado:
            if getattr(cambio, "fechaHoraFin", None) is not None and not getattr(cambio, "_fin_persisted", False):
                if getattr(cambio, "_db_id", None):
                    dao.update_field(cambio._db_id, 'fechaHoraFin', cambio.fechaHoraFin)
                    cambio._fin_persisted = True
                else:
                    q = session.query(CambioEstadoModel).filter_by(fechaHoraInicio=cambio.fechaHoraInicio)
                    if hasattr(cambio.responsableInspeccion, "get_db_id") and cambio.responsableInspeccion.get_db_id():
                        q = q.filter_by(responsableInspeccion_id=cambio.responsableInspeccion.get_db_id())
                    modelo = q.first()
                    if modelo:
                        modelo.fechaHoraFin = cambio.fechaHoraFin
                        session.commit()
                        cambio._db_id = modelo.id
                        cambio._fin_persisted = True
        dao.close()

    @staticmethod
    def create_new_change(cambio_entity, evento_entity):
        """
        Persiste un nuevo CambioEstado asociado a la entidad EventoSismico.
        Devuelve el modelo creado.
        """
        modelo = cambio_to_model(cambio_entity, evento=evento_entity)
        dao = BaseDAO(CambioEstadoModel)
        created = dao.create(modelo)
        try:
            cambio_entity._db_id = created.id
        except Exception:
            cambio_entity._db_id = getattr(created, "id", None)
        dao.close()
        return created

    @staticmethod
    def update_change_fecha_fin(cambio_entity):
        """
        Actualiza fechaHoraFin de un CambioEstado ya persistido.
        """
        dao = BaseDAO(CambioEstadoModel)
        if getattr(cambio_entity, "_db_id", None):
            dao.update_field(cambio_entity._db_id, 'fechaHoraFin', cambio_entity.fechaHoraFin)
            cambio_entity._fin_persisted = True
        else:
            # fallback: buscar por heurística
            session = dao.db
            q = session.query(CambioEstadoModel).filter_by(fechaHoraInicio=cambio_entity.fechaHoraInicio)
            if hasattr(cambio_entity.responsableInspeccion, "get_db_id") and cambio_entity.responsableInspeccion.get_db_id():
                q = q.filter_by(responsableInspeccion_id=cambio_entity.responsableInspeccion.get_db_id())
            modelo = q.first()
            if modelo:
                modelo.fechaHoraFin = cambio_entity.fechaHoraFin
                session.commit()
                cambio_entity._db_id = modelo.id
                cambio_entity._fin_persisted = True
        dao.close()
