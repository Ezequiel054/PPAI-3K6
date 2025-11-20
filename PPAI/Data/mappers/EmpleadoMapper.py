from ClasesEntidad.Empleado import Empleado
from Data.models.Empleado import EmpleadoModel

def model_to_empleado(model):
    emp = Empleado(model.nombre, model.apellido)
    # almacenar id de BD en atributo privado para uso interno de la capa de persistencia
    emp._db_id = getattr(model, "id", None)
    return emp

def empleado_to_model(obj):
    return EmpleadoModel(nombre=obj.nombre, apellido=obj.apellido)

