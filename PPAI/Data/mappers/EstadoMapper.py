# mapper_estado.py
from ClasesEntidad.Estado import Estado
from Data.models.Estado import EstadoModel
from ClasesEntidad.State.Rechazado import Rechazado

def model_to_estado(model):
    """
    Convierte EstadoModel -> una subclase concreta de Estado según el nombre guardado en la BD.
    Ejemplo: si nombreEstado = "AutoDetectado", devolverá EstadoAutoDetectado(ambito)
    """
    if model is None:
        return None

    id = getattr(model, "id", None)
    ambito = getattr(model, "ambito", None)
    nombre_estado = getattr(model, "nombreEstado", None)
    if (nombre_estado == "AutoDetectado"):
        from ClasesEntidad.State.AutoDetectado import AutoDetectado
        inst = AutoDetectado(ambito, id)
        return inst
    elif (nombre_estado == "BloqueadoEnRevision"):
        from ClasesEntidad.State.BloqueadoEnRevision import BloqueadoEnRevision
        inst = BloqueadoEnRevision(ambito, id)
        return inst
    elif (nombre_estado == "Rechazado"):
        inst = Rechazado(ambito, id)
        return inst
    else:
        return None

    # # Buscamos todas las subclases de Estado
    # subclases = {cls.__name__: cls for cls in Estado.__subclasses__()}

    # # Buscamos si existe una subclase con el mismo nombre
    # clase_estado = subclases.get(nombre_estado)

    # if clase_estado:
    #     # Si la encontramos, la instanciamos normalmente
    #     return clase_estado(ambito)
    # else:
    #     # Si no existe esa subclase, usamos una genérica
    #     class EstadoDesconocido(Estado):
    #         def __init__(self, ambito, nombre):
    #             super().__init__(ambito)
    #             self.nombreEstado = nombre

    #         def __repr__(self):
    #             return f"<EstadoDesconocido(nombreEstado={self.nombreEstado})>"

    #     return EstadoDesconocido(ambito, nombre_estado)


def estado_to_model(obj):
    """
    Convierte una instancia de Estado (o subclase) -> EstadoModel.
    Guarda el nombre de la clase como nombreEstado.
    """
    if obj is None:
        return None

    if isinstance(obj, EstadoModel):
        return obj

    ambito = getattr(obj, "ambito", None)
    nombre_estado = getattr(obj, "nombreEstado", obj.__class__.__name__)

    return EstadoModel(ambito=ambito, nombreEstado=nombre_estado)
