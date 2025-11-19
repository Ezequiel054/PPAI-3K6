from ClasesEntidad.DetalleMuestraSismica import DetalleMuestraSismica
from Data.models.DetalleMuestraSismica import DetalleMuestraSismicaModel
from Data.mappers.TipoDeDatoMapper import model_to_tipo, tipo_to_model

def model_to_detalle(model):
    tipo = model_to_tipo(model.tipoDeDato) if hasattr(model, "tipoDeDato") and model.tipoDeDato else None
    return DetalleMuestraSismica(model.valor, tipo)

def detalle_to_model(obj):
    return DetalleMuestraSismicaModel(
        valor=obj.valor,
        tipoDeDato=tipo_to_model(obj.tipoDeDato) if hasattr(obj, "tipoDeDato") and obj.tipoDeDato else None
    )

