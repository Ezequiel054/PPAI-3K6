from ClasesEntidad.Sismografo import Sismografo
from Data.models.Sismografo import SismografoModel
from Data.mappers.EstacionSismologicaMapper import model_to_estacion
from Data.mappers.SerieTemporalMapper import model_to_serie


def model_to_sismografo(model):
    estacion = model_to_estacion(model.estacionSismologica) if hasattr(model, "estacionSismologica") and model.estacionSismologica else None
    serie = model_to_serie(model.serieTemporal) if hasattr(model, "serieTemporal") and model.serieTemporal else None
    return Sismografo(
        model.fechaAdquisicion,
        model.identificadorSismografo,
        model.nroSerie,
        estacion,
        serie
    )

def sismografo_to_model(obj):
    return SismografoModel(
        fechaAdquisicion=obj.fechaAdquisicion,
        identificadorSismografo=obj.identificadorSismografo,
        nroSerie=obj.nroSerie
    )

