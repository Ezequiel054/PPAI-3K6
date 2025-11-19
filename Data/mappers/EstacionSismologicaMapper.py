from ClasesEntidad.EstacionSismologica import EstacionSismologica
from Data.models.EstacionSismologica import EstacionSismologicaModel


def model_to_estacion(model):
    return EstacionSismologica(
        model.codigoEstacion,
        model.nombre,
        model.latitud,
        model.longitud,
        model.nroCertificacionAdquisicion,
        model.documentoCertificacionAdq,
        model.fechaSolcitudCertificacion
    )

def estacion_to_model(obj):
    return EstacionSismologicaModel(
        codigoEstacion=obj.codigoEstacion,
        nombre=obj.nombre,
        latitud=obj.latitud,
        longitud=obj.longitud,
        nroCertificacionAdquisicion=obj.nroCertificacionAdquisicion,
        documentoCertificacionAdq=obj.documentoCertificacionAdq,
        fechaSolcitudCertificacion=obj.fechaSolcitudCertificacion
    )

