from Data.models.CambioEstado import CambioEstadoModel
from Data.mappers.EstadoMapper import estado_to_model
from Data.mappers.EmpleadoMapper import empleado_to_model

def model_to_cambio(model):
    from ClasesEntidad.CambioEstado import CambioEstado
    cambio = CambioEstado(
        model.fechaHoraInicio,
        model.fechaHoraFin,
        model.estado,
        model.responsableInspeccion
    )
    # conservar id de BD en atributo privado
    cambio._db_id = getattr(model, "id", None)
    return cambio

def cambio_to_model(obj, evento=None):
    """
    Convierte una entidad CambioEstado -> CambioEstadoModel.
    Si se recibe 'evento' (entidad EventoSismico), intentará resolver eventoSismico_id a partir de:
      1) evento.get_db_id()
      2) búsqueda en BD por atributos distintivos del evento (fallback)
    """
    from Data.database import SessionLocal
    from Data.models.Estado import EstadoModel
    from Data.models.Empleado import EmpleadoModel
    from Data.models.EventoSismico import EventoSismicoModel

    session = SessionLocal()

    # Estado
    estado_id = None
    if hasattr(obj.estado, "get_db_id") and obj.estado.get_db_id():
        estado_id = obj.estado.get_db_id()
    else:
        estado_row = session.query(EstadoModel).filter_by(nombreEstado=getattr(obj.estado, "nombreEstado", None),
                                                          ambito=getattr(obj.estado, "ambito", None)).first()
        estado_id = estado_row.id if estado_row else None

    # Responsable (Empleado)
    responsable_id = None
    if hasattr(obj.responsableInspeccion, "get_db_id") and obj.responsableInspeccion.get_db_id():
        responsable_id = obj.responsableInspeccion.get_db_id()
    else:
        empleado_row = session.query(EmpleadoModel).filter_by(nombre=getattr(obj.responsableInspeccion, "nombre", None),
                                                              apellido=getattr(obj.responsableInspeccion, "apellido", None)).first()
        responsable_id = empleado_row.id if empleado_row else None

    # EventoSismico -> resolver id
    evento_id = None
    if evento is not None:
        if hasattr(evento, "get_db_id") and evento.get_db_id():
            evento_id = evento.get_db_id()
        else:
            # intentar buscar por campos distintivos del evento
            evento_row = session.query(EventoSismicoModel).filter_by(
                fechaHoraOcurrencia=getattr(evento, "fechaHoraOcurrencia", None),
                valorMagnitud=getattr(evento, "valorMagnitud", None)
            ).first()
            if evento_row:
                evento_id = evento_row.id

    # Si no se pasó evento y obj tiene referencia interna, intentar detectar (no obligatorio)
    if evento_id is None:
        # buscar por fechaHoraInicio del cambio y responsable para relacionarlo con algún evento (muy heurístico)
        posible = session.query(CambioEstadoModel).filter_by(fechaHoraInicio=obj.fechaHoraInicio,
                                                             responsableInspeccion_id=responsable_id).first()
        if posible:
            evento_id = posible.eventoSismico_id

    session.close()

    model_kwargs = {
        "fechaHoraInicio": obj.fechaHoraInicio,
        "fechaHoraFin": obj.fechaHoraFin,
        "estado_id": estado_id,
        "responsableInspeccion_id": responsable_id,
        "eventoSismico_id": evento_id
    }

    obj_db_id = getattr(obj, "_db_id", None)
    if obj_db_id:
        model_kwargs["id"] = obj_db_id

    return CambioEstadoModel(**model_kwargs)

