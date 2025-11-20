from Data.models.CambioEstado import CambioEstadoModel

def model_to_cambio(model):
    from ClasesEntidad.CambioEstado import CambioEstado
    cambio = CambioEstado(
        model.fechaHoraInicio,
        model.fechaHoraFin,
        # mapear Estado/Empleado como modelos (las entidades pueden requerir mappers si se necesitan)
        getattr(model, "estado", None),
        getattr(model, "responsableInspeccion", None)
    )
    # No asignar id ni _db_id a la entidad (dominio no maneja ids)
    return cambio

def cambio_to_model(obj, evento_id=None):
    """
    Mapper sencillo: no hace inferencias ni accesos a BD.
    Requiere que las entidades relacionadas (estado, responsableInspeccion) tengan 'id' en sus MODELS
    si se quiere persistir la FK; el mapper recibe evento_id cuando procede desde el DAO.
    """
    kwargs = {
        "fechaHoraInicio": obj.fechaHoraInicio,
        "fechaHoraFin": obj.fechaHoraFin,
        "estado_id": getattr(getattr(obj, "estado", None), "id", None),
        "responsableInspeccion_id": getattr(getattr(obj, "responsableInspeccion", None), "id", None),
        "eventoSismico_id": evento_id
    }
    # No leer ni pasar id desde la entidad de dominio
    return CambioEstadoModel(**kwargs)

