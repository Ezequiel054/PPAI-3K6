from ClasesEntidad.SerieTemporal import SerieTemporal
from Data.models.SerieTemporal import SerieTemporalModel
from Data.mappers.MuestraSismicaMapper import model_to_muestra

def model_to_serie(model):
    muestras = [model_to_muestra(m) for m in model.muestraSismica] if hasattr(model, "muestraSismica") and model.muestraSismica else []
    return SerieTemporal(
        model.condicionAlarma,
        model.fechaHoraInicioRegistroMuestras,
        model.fechaHoraRegistro,
        model.frecuenciaMuestreo,
        muestras
    )

def serie_to_model(obj):
    return SerieTemporalModel(
        condicionAlarma=obj.condicionAlarma,
        fechaHoraInicioRegistroMuestras=obj.fechaHoraInicioRegistroMuestras,
        fechaHoraRegistro=obj.fechaHoraRegistro,
        frecuenciaMuestreo=obj.frecuenciaMuestreo
    )
