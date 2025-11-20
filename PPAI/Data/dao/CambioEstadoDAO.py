from Data.database import SessionLocal
from Data.mappers.CambioDeEstadoMapper import cambio_to_model


class CambioEstadoDAO:
    def guardar(self, cambio, evento=None):
        """
        Persiste un CambioEstado (entidad) usando el mapper.
        Si se pasa 'evento', se lo utiliza para resolver ids en el mapper.
        """
        session = SessionLocal()
        try:
            modelo = cambio_to_model(cambio, evento=evento)
            merged = session.merge(modelo)
            session.commit()
            session.refresh(merged)
            try:
                cambio._db_id = merged.id
            except Exception:
                cambio._db_id = getattr(merged, "id", None)
            return merged
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    def guardarCambiosDeEvento(self, evento):
        session = SessionLocal()
        try:
            for cambio in getattr(evento, "cambiosEstado", []) or []:
                if getattr(cambio, "_db_id", None):
                    continue
                modelo = cambio_to_model(cambio, evento=evento)
                merged = session.merge(modelo)
                session.flush()
                cambio._db_id = getattr(merged, "id", None)
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()
