from Data.database import SessionLocal
from Data.models.EventoSismico import EventoSismicoModel
from Data.models.CambioEstado import CambioEstadoModel
from Data.models.Estado import EstadoModel
from Data.models.Empleado import EmpleadoModel
from Data.mappers.EventoSismicoMapper import evento_to_model, model_to_evento
from Data.mappers.CambioDeEstadoMapper import cambio_to_model
from Data.dao.EstadoDAO import EstadoDAO


class EventoDAO:
    def guardar(self, evento):
        """
        Actualiza un Evento existente (no crea nuevos eventos).
        - Busca el evento en BD por campos distintivos (fechaHoraOcurrencia + valorMagnitud).
        - Actualiza campos permitidos y persiste nuevos CambiosEstado vinculados al evento.
        - Devuelve la entidad de dominio reconstruida desde BD.
        """
        session = SessionLocal()
        try:
            # Buscar evento ya existente (evitar crear nuevos registros)
            existing = session.query(EventoSismicoModel).filter_by(
                fechaHoraOcurrencia=getattr(evento, "fechaHoraOcurrencia", None),
                valorMagnitud=getattr(evento, "valorMagnitud", None)
            ).first()

            if existing is None:
                # Política: NO crear eventos nuevos desde este DAO.
                raise ValueError("Evento no existe en BD; EventoDAO.guardar solo actualiza eventos existentes.")

            # Actualizar campos permisibles (solo memoria/BD)
            existing.fechaHoraFin = getattr(evento, "fechaHoraFin", existing.fechaHoraFin)
            existing.latitudEpicentro = getattr(evento, "latitudEpicentro", existing.latitudEpicentro)
            existing.latitudHipocentro = getattr(evento, "latitudHipocentro", existing.latitudHipocentro)
            existing.longitudEpicentro = getattr(evento, "longitudEpicentro", existing.longitudEpicentro)
            existing.longitudHipocentro = getattr(evento, "longitudHipocentro", existing.longitudHipocentro)
            existing.valorMagnitud = getattr(evento, "valorMagnitud", existing.valorMagnitud)

            # Resolver estadoActual: buscar si existe un Estado coincidente y asignar FK
            if getattr(evento, "estadoActual", None):
                estado_dao = EstadoDAO(session=session)
                existing_estado = estado_dao.find_by_nombre_y_ambito(evento.estadoActual.nombreEstado, evento.estadoActual.ambito)
                if existing_estado:
                    existing.estadoActual_id = existing_estado.id

            session.flush()

            # Persistir CambiosEstado nuevos (heurística: por fechaHoraInicio + evento_id)
            for cambio in getattr(evento, "cambiosEstado", []) or []:
                # ver si ya existe ese cambio para este evento
                exist_cambio = session.query(CambioEstadoModel).filter_by(
                    fechaHoraInicio=getattr(cambio, "fechaHoraInicio", None),
                    eventoSismico_id=existing.id
                ).first()
                if exist_cambio:
                    continue  # ya persistido

                # resolver fk estado_id
                estado_row = None
                if getattr(cambio, "estado", None):
                    estado_row = session.query(EstadoModel).filter_by(
                        nombreEstado=getattr(cambio.estado, "nombreEstado", None),
                        ambito=getattr(cambio.estado, "ambito", None)
                    ).first()

                # resolver fk responsableInspeccion_id
                responsable_row = None
                if getattr(cambio, "responsableInspeccion", None):
                    responsable_row = session.query(EmpleadoModel).filter_by(
                        nombre=getattr(cambio.responsableInspeccion, "nombre", None),
                        apellido=getattr(cambio.responsableInspeccion, "apellido", None)
                    ).first()

                cambio_model = CambioEstadoModel(
                    fechaHoraInicio=cambio.fechaHoraInicio,
                    fechaHoraFin=cambio.fechaHoraFin,
                    estado_id=getattr(estado_row, "id", None),
                    responsableInspeccion_id=getattr(responsable_row, "id", None),
                    eventoSismico_id=existing.id
                )
                session.add(cambio_model)

            # Commit único
            session.commit()
            session.refresh(existing)
            return model_to_evento(existing)
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
            modelos = session.query(EventoSismicoModel).join("estadoActual").filter_by(nombreEstado="AutoDetectado").all()
            return [model_to_evento(m) for m in modelos]
        finally:
            session.close()
