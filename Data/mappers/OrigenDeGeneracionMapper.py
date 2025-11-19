from ClasesEntidad.OrigenDeGeneracion import OrigenDeGeneracion
from Data.models.OrigenDeGeneracion import OrigenDeGeneracionModel

def model_to_origen(model):
    return OrigenDeGeneracion(model.nombre, model.descripcion)

def origen_to_model(obj):
    return OrigenDeGeneracionModel(nombre=obj.nombre, descripcion=obj.descripcion)
