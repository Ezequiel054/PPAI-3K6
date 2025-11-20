from Data.database import SessionLocal
from Data.models.EventoSismico import EventoSismicoModel
from Data.models.Estado import EstadoModel
from Data.mappers.EventoSismicoMapper import evento_to_model, model_to_evento
from Data.mappers.CambioDeEstadoMapper import cambio_to_model
from Data.mappers.EstadoMapper import estado_to_model


class EventoDAO:
    def guardar(self, evento):
        """
        Persiste/actualiza un Evento y sus CambiosEstado en una única transacción.
        Usa los mappers existentes para convertir entidad -> modelo.
        Devuelve la entidad reconstruida desde la BD (opcional).
        """
        session = SessionLocal()
        try:
            # 1) Convertir evento -> modelo (relaciones incluidas)
            evento_model = evento_to_model(evento)

            # 2) Merge del evento (insert/update)
            merged_event = session.merge(evento_model)
            session.flush()

            # 3) Asegurar persistencia de cambios de estado recién creados en memoria
            for cambio in getattr(evento, "cambiosEstado", []) or []:
                # si ya tiene _db_id asumimos persistido
                if getattr(cambio, "_db_id", None):
                    continue
                # uso del mapper para resolver ids (estado, responsable, evento) heurísticamente
                cambio_model = cambio_to_model(cambio, evento=evento)
                merged_cambio = session.merge(cambio_model)
                session.flush()
                # asignar back el id persistido a la entidad en memoria
                try:
                    cambio._db_id = merged_cambio.id
                except Exception:
                    cambio._db_id = getattr(merged_cambio, "id", None)

            # 4) Actualizar referencia estadoActual_id si la entidad tiene estadoActual
            if getattr(evento, "estadoActual", None):
                estado_model = estado_to_model(evento.estadoActual)
                # intentar encontrar un registro existente
                existing = session.query(EstadoModel).filter_by(
                    nombreEstado=estado_model.nombreEstado, ambito=estado_model.ambito
                ).first()
                if existing:
                    merged_event.estadoActual_id = existing.id
                else:
                    new_estado = session.merge(estado_model)
                    session.flush()
                    merged_event.estadoActual_id = new_estado.id

            # 5) Commit único
            session.commit()
            session.refresh(merged_event)
            # devolver entidad reconstruida desde BD para consistencia
            return model_to_evento(merged_event)
        except Exception as ex:
            session.rollback()
            print("Error en EventoDAO.guardar:", ex)
            raise
        finally:
            session.close()

    def buscarPorId(self, id_):
        session = SessionLocal()
        try:
            modelo = session.query(EventoSismicoModel).filter_by(id=id_).first()
            return model_to_evento(modelo) if modelo else None
        finally:
            session.close()

    def actualizar(self, evento):
        # simple alias a guardar para este diseño
        return self.guardar(evento)

    def listarAutodetectados(self):
        """
        Devuelve lista de entidades Evento que tengan estado 'AutoDetectado'
        (se apoya en el campo Estado.nombreEstado).
        """
        session = SessionLocal()
        try:
            # join por relación: Estado.nombreEstado == "AutoDetectado"
            modelos = session.query(EventoSismicoModel).join(EstadoModel, EventoSismicoModel.estadoActual_id == EstadoModel.id)\
                .filter(EstadoModel.nombreEstado == "AutoDetectado").all()
            return [model_to_evento(m) for m in modelos]
        finally:
            session.close()
