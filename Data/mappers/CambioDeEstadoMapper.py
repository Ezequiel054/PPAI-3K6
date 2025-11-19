from Data.models.CambioEstado import CambioEstadoModel
from Data.mappers.EstadoMapper import estado_to_model
from Data.mappers.EmpleadoMapper import empleado_to_model

def model_to_cambio(model):
    from ClasesEntidad.CambioEstado import CambioEstado
    return CambioEstado(
        model.fechaHoraInicio,
        model.fechaHoraFin,
        model.estado,
        model.responsableInspeccion,
        model.id
    )

def cambio_to_model(obj):
    if (obj.id != 0):
        return CambioEstadoModel(
            fechaHoraInicio=obj.fechaHoraInicio,
            fechaHoraFin=obj.fechaHoraFin,
            estado_id=obj.estado.id,
            responsableInspeccion_id=obj.responsableInspeccion.id,
            id=obj.id
        )
    
    return CambioEstadoModel(
        fechaHoraInicio=obj.fechaHoraInicio,
        fechaHoraFin=obj.fechaHoraFin,
        estado_id=obj.estado.id,
        responsableInspeccion_id=obj.responsableInspeccion.id
    )

