from Data.dao.baseDao import BaseDAO
from Data.models.CambioEstado import CambioEstadoModel
from Data.mappers.CambioDeEstadoMapper import cambio_to_model

class CambioEstado:
    def __init__(self, fechaHoraInicio, fechaHoraFin, estado, responsableInspeccion, id=None):
        self.fechaHoraInicio = fechaHoraInicio
        self.fechaHoraFin = fechaHoraFin
        self.estado = estado
        self.responsableInspeccion = responsableInspeccion
        self.id = id


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

    def saveInDB(self):
        dao = BaseDAO(CambioEstadoModel)
        dao.create(cambio_to_model(self))

