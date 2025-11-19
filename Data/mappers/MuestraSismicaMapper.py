from ClasesEntidad.MuestraSismica import MuestraSismica
from Data.models.MuestraSismica import MuestraSismicaModel
from Data.mappers.DetalleMuestraSismicaMapper import model_to_detalle, detalle_to_model

def model_to_muestra(model):
    detalle = model_to_detalle(model.detalleMuestraSismica) if hasattr(model, "detalleMuestraSismica") and model.detalleMuestraSismica else None
    return MuestraSismica(model.fechaHoraMuestra, detalle)

def muestra_to_model(obj):
    return MuestraSismicaModel(
        fechaHoraMuestra=obj.fechaHoraMuestra,
        detalleMuestraSismica=detalle_to_model(obj.detalleMuestraSismica) if hasattr(obj, "detalleMuestraSismica") and obj.detalleMuestraSismica else None
    )