from Data.models.ClasificacionSismo import ClasificacionSismoModel
from ClasesEntidad.ClasificacionSismo import ClasificacionSismo


def model_to_clasificacion(model):
    return ClasificacionSismo(
        nombre=model.nombre,
        kmDesde=model.kmProfundidadDesde,
        kmHasta=model.kmProfundidadHasta
    )

def clasificacion_to_model(obj):
    return ClasificacionSismoModel(
        kmProfundidadDesde=obj.kmProfundidadDesde,
        kmProfundidadHasta=obj.kmProfundidadHasta
    )
