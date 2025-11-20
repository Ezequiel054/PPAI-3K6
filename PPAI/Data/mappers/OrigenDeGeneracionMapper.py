from ClasesEntidad.OrigenDeGeneracion import OrigenDeGeneracion
from Data.models.OrigenDeGeneracion import OrigenDeGeneracionModel

def model_to_origen(model):
    origen = OrigenDeGeneracion(model.nombre, model.descripcion)
    origen._db_id = getattr(model, "id", None)
    return origen

def origen_to_model(obj):
    return OrigenDeGeneracionModel(nombre=obj.nombre, descripcion=obj.descripcion)
