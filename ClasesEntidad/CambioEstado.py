from Data.dao.baseDao import BaseDAO
from Data.models.CambioEstado import CambioEstadoModel
from Data.mappers.CambioDeEstadoMapper import cambio_to_model

class CambioEstado:
    def __init__(self, fechaHoraInicio, fechaHoraFin, estado, responsableInspeccion, id=None):
        self.fechaHoraInicio = fechaHoraInicio
        self.fechaHoraFin = fechaHoraFin
        self.estado = estado
        self.responsableInspeccion = responsableInspeccion

    def __str__(self):
        return f"\nCambioEstado({self.fechaHoraInicio}, {self.fechaHoraFin}, {self.estado.nombreEstado}, {self.responsableInspeccion.nombre})\n"

    def esEstadoActual(self):
        return self.fechaHoraFin is None


    def setFechaFin(self, fechaFin):
        self.fechaHoraFin = fechaFin
        self.updateInDB(fechaFin)
    
    def updateInDB(self, fechaFin):
        dao = BaseDAO(CambioEstadoModel)
        print("Fecha")
        print(fechaFin)
        print("Fecha")
        dao.update_field(self.id, 'fechaHoraFin', fechaFin)

    def saveInDB(self, eventoSismico_id):
        dao = BaseDAO(CambioEstadoModel)
        modelo = cambio_to_model(self)
        modelo.eventoSismico_id = eventoSismico_id
        created_model = dao.create(modelo)
        # Pisa el id None con el id asignado por la BD
        try:
            self.id = created_model.id
        except Exception:
            # fallback por si el modelo tiene otra forma de exponer el id
            self.id = getattr(created_model, "id", self.id)

    # def saveInDB(self):
    #     dao = BaseDAO(CambioEstadoModel)
    #     # Al crear el registro en la BD, el DAO devuelve el modelo SQLAlchemy con el id asignado.
    #     created_model = dao.create(cambio_to_model(self))
    #     # Asegurarse de propagar el id asignado al objeto dominio para futuras actualizaciones.
    #     try:
    #         self.id = created_model.id
    #     except Exception:
    #         # fallback por si el modelo tiene otra forma de exponer el id
    #         self.id = getattr(created_model, "id", self.id)
    #     return created_model

