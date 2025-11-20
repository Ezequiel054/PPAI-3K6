from Data.models.AlcanceSismo import AlcanceSismoModel
from ClasesEntidad.AlcanceSismo import AlcanceSismo


def model_to_alcance(model):
    alcance = AlcanceSismo(model.nombre, model.descripcion)
    alcance._db_id = getattr(model, "id", None)
    return alcance

def alcance_to_model(obj):
    return AlcanceSismoModel(nombre=obj.nombre, descripcion=obj._descripcion)