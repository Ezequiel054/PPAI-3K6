from Data.models.AlcanceSismo import AlcanceSismoModel
from ClasesEntidad.AlcanceSismo import AlcanceSismo


def model_to_alcance(model):
    return AlcanceSismo(model.nombre, model.descripcion)

def alcance_to_model(obj):
    return AlcanceSismoModel(nombre=obj.nombre, descripcion=obj._descripcion)