from ClasesEntidad.EstacionSismologica import EstacionSismologica
from Data.models.EstacionSismologica import EstacionSismologicaModel


def model_to_estacion(model):
    est = EstacionSismologica(
        model.codigoEstacion,
        model.nombre,
        model.latitud,
        model.longitud,
        model.nroCertificacionAdquisicion,
        model.documentoCertificacionAdq,
        model.fechaSolcitudCertificacion
    )
    est._db_id = getattr(model, "id", None)
    return est

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

