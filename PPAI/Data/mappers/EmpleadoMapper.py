from ClasesEntidad.Empleado import Empleado
from Data.models.Empleado import EmpleadoModel

def model_to_empleado(model):
    emp = Empleado(model.nombre, model.apellido)
    # no llamar a emp._set_db_id(...) desde mappers porque las entidades no exponen esa API
    # si se desea mantener el id para uso interno, hacerlo como `emp._db_id = model.id` (no obligatorio)
    return emp

def empleado_to_model(obj):
    return EmpleadoModel(nombre=obj.nombre, apellido=obj.apellido)

