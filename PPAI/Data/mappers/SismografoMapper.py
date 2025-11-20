from ClasesEntidad.Sismografo import Sismografo
from Data.models.Sismografo import SismografoModel
from Data.mappers.EstacionSismologicaMapper import model_to_estacion
from Data.mappers.SerieTemporalMapper import model_to_serie


def model_to_sismografo(model):
    series = []
    if hasattr(model, "serieTemporal") and model.serieTemporal:
        series = [model_to_serie(s) for s in model.serieTemporal]

    estacion = model_to_estacion(model.estacionSismologica) if hasattr(model, "estacionSismologica") and model.estacionSismologica else None
    s = Sismografo(
        model.fechaAdquisicion,
        model.identificadorSismografo,
        model.nroSerie,
        estacion,
        series  # lista de series
    )
    s._db_id = getattr(model, "id", None)
    print("Estacion mapeada:", estacion)
    return s


def sismografo_to_model(obj):
    return SismografoModel(
        fechaAdquisicion=obj.fechaAdquisicion,
        identificadorSismografo=obj.identificadorSismografo,
        nroSerie=obj.nroSerie
    )

