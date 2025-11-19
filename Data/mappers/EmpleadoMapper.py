from ClasesEntidad.Empleado import Empleado
from Data.models.Empleado import EmpleadoModel

def model_to_empleado(model):
    return Empleado(model.nombre, model.apellido, model.id)

def empleado_to_model(obj):
    return EmpleadoModel(nombre=obj.nombre, apellido=obj.apellido)

