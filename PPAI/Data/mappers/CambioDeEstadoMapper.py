from ClasesEntidad.CambioEstado import CambioEstado
from Data.models.CambioEstado import CambioEstadoModel


def model_to_cambio(model):
    return CambioEstado(
        model.fechaHoraInicio,
        model.fechaHoraFin,
        model.estado,
        model.responsableInspeccion
    )

def cambio_to_model(obj):
    return CambioEstadoModel(
        fechaHoraInicio=obj.fechaHoraInicio,
        fechaHoraFin=obj.fechaHoraFin,
        estado=obj.estado,
        responsableInspeccion=obj.responsableInspeccion
    )

