from ClasesEntidad.TipoDeDato import TipoDeDato
from Data.models.TipoDeDato import TipoDeDatoModel

def model_to_tipo(model):
    tipo = TipoDeDato(model.denominacion, model.nombreUnidadMedida, model.valorUmbral)
    tipo._db_id = getattr(model, "id", None)
    return tipo

def tipo_to_model(obj):
    return TipoDeDatoModel(
        denominacion=obj.denominacion,
        nombreUnidadMedida=obj.nombreUnidadMedida,
        valorUmbral=obj.valorUmbral
    )
