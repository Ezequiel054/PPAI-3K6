from Data.database import SessionLocal
from Data.mappers.CambioDeEstadoMapper import cambio_to_model


class CambioEstadoDAO:
    def guardar(self, cambio, evento_id=None):
        """
        Persiste un CambioEstado (entidad) usando el mapper simple.
        evento_id puede pasarse si el cambio pertenece a un evento.
        """
        session = SessionLocal()
        try:
            modelo = cambio_to_model(cambio, evento_id=evento_id)
            merged = session.merge(modelo)
            session.commit()
            session.refresh(merged)
            # NO asignar id a la entidad de dominio (id queda en el modelo/BD)
            return merged
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()
