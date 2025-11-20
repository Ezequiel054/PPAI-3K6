from ClasesEntidad.DetalleMuestraSismica import DetalleMuestraSismica
from Data.models.DetalleMuestraSismica import DetalleMuestraSismicaModel
from Data.mappers.TipoDeDatoMapper import model_to_tipo, tipo_to_model

def model_to_detalle(model):
    tipo = model_to_tipo(model.tipoDeDato) if hasattr(model, "tipoDeDato") and model.tipoDeDato else None
    det = DetalleMuestraSismica(model.valor, tipo)
    det._db_id = getattr(model, "id", None)
    return det

def detalle_to_model(obj):
    return DetalleMuestraSismicaModel(
        valor=obj.valor,
        tipoDeDato=tipo_to_model(obj.tipoDeDato) if hasattr(obj, "tipoDeDato") and obj.tipoDeDato else None
    )

