from ClasesEntidad.Usuario import Usuario
from Data.models.Usuario import UsuarioModel
from Data.mappers.EmpleadoMapper import model_to_empleado, empleado_to_model


def model_to_usuario(model):
    empleado = model_to_empleado(model.empleado) if hasattr(model, "empleado") and model.empleado else None
    u = Usuario(model.nombreUsuario, model.password, empleado)
    # No asignar ids a la entidad de dominio
    return u

def usuario_to_model(obj):
    return UsuarioModel(
        nombreUsuario=obj.nombreUsuario,
        password=obj.password,
        empleado=empleado_to_model(obj.empleado) if hasattr(obj, "empleado") and obj.empleado else None
    )

