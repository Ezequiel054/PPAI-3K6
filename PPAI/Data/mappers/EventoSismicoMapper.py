from ClasesEntidad.EventoSismico import EventoSismico
from Data.models.EventoSismico import EventoSismicoModel

from Data.mappers.ClasificacionSismoMapper import model_to_clasificacion, clasificacion_to_model
from Data.mappers.OrigenDeGeneracionMapper import model_to_origen, origen_to_model
from Data.mappers.AlcanceSismoMapper import model_to_alcance, alcance_to_model
from Data.mappers.SerieTemporalMapper import model_to_serie, serie_to_model
from Data.mappers.CambioDeEstadoMapper import model_to_cambio, cambio_to_model
from Data.mappers.EstadoMapper import model_to_estado, estado_to_model


def model_to_evento(model):
    """Convierte un EventoSismicoModel -> EventoSismico (entidad de dominio)."""
    if model is None:
        return None

    Evento = EventoSismico(
        model.fechaHoraOcurrencia,
        model.fechaHoraFin,
        model.latitudEpicentro,
        model.latitudHipocentro,
        model.longitudEpicentro,
        model.longitudHipocentro,
        model.valorMagnitud,
        model_to_clasificacion(model.clasificacionSismo) if getattr(model, "clasificacionSismo", None) else None,
        model_to_origen(model.origenGeneracion) if getattr(model, "origenGeneracion", None) else None,
        model_to_alcance(model.alcanceSismo) if getattr(model, "alcanceSismo", None) else None,
        [model_to_serie(s) for s in getattr(model, "series", [])],
        model_to_estado(model.estadoActual) if getattr(model, "estadoActual", None) else None,
        [model_to_cambio(c) for c in getattr(model, "cambiosEstado", [])]
    )

    # NO asignar id a la entidad de dominio
    return Evento

def evento_to_model(obj):
    """Convierte un EventoSismico (entidad) -> EventoSismicoModel (modelo SQLAlchemy)."""
    if obj is None:
        return None

    model = EventoSismicoModel(
        fechaHoraOcurrencia=obj.fechaHoraOcurrencia,
        fechaHoraFin=obj.fechaHoraFin,
        latitudEpicentro=obj.latitudEpicentro,
        latitudHipocentro=obj.latitudHipocentro,
        longitudEpicentro=obj.longitudEpicentro,
        longitudHipocentro=obj.longitudHipocentro,
        valorMagnitud=obj.valorMagnitud,
    )

    # Relaciones (clasificacion, origen, alcance) - se mantienen
    model.clasificacionSismo = clasificacion_to_model(obj.clasificacion) if getattr(obj, "clasificacion", None) else None
    model.origenGeneracion = origen_to_model(obj.origenGeneracion) if getattr(obj, "origenGeneracion", None) else None
    model.alcanceSismo = alcance_to_model(obj.alcanceSismo) if getattr(obj, "alcanceSismo", None) else None
    # NOTA: no asignar model.estadoActual aquí; el DAO decide la FK usando EstadoDAO.

    # Relaciones 1 a muchos: no leer id de la entidad (evento no tiene id en dominio)
    model.series = [serie_to_model(s) for s in getattr(obj, "serieTemporal", [])]
    model.cambiosEstado = [cambio_to_model(c, evento_id=None) for c in getattr(obj, "cambiosEstado", [])]

    return model
