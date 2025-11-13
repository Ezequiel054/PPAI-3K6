from ClasesEntidad.Sesion import Sesion
from Data.models.Sesion import SesionModel
from Data.mappers.UsuarioMapper import model_to_usuario, usuario_to_model

def model_to_sesion(model):
    usuario = model_to_usuario(model.usuario) if hasattr(model, "usuario") and model.usuario else None
    return Sesion(model.fechaHoraDesde, model.fechaHoraHasta, usuario)

def sesion_to_model(obj):
    return SesionModel(
        fechaHoraDesde=obj.fechaHoraDesde,
        fechaHoraHasta=obj.fechaHoraHasta,
        usuario=usuario_to_model(obj.usuario) if hasattr(obj, "usuario") and obj.usuario else None
    )

