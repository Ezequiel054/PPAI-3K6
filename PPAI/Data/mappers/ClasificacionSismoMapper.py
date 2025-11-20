from Data.models.ClasificacionSismo import ClasificacionSismoModel
from ClasesEntidad.ClasificacionSismo import ClasificacionSismo


def model_to_clasificacion(model):
    clas = ClasificacionSismo(
        nombre=model.nombre,
        kmDesde=model.kmProfundidadDesde,
        kmHasta=model.kmProfundidadHasta
    )
    clas._db_id = getattr(model, "id", None)
    return clas

def clasificacion_to_model(obj):
    return ClasificacionSismoModel(
        kmProfundidadDesde=obj.kmProfundidadDesde,
        kmProfundidadHasta=obj.kmProfundidadHasta
    )
