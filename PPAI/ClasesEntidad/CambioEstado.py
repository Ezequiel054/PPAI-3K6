class CambioEstado:
    def __init__(self, fechaHoraInicio, fechaHoraFin, estado, responsableInspeccion):
        self.fechaHoraInicio = fechaHoraInicio
        self.fechaHoraFin = fechaHoraFin
        self.estado = estado
        self.responsableInspeccion = responsableInspeccion


    def esEstadoActual(self):
        return self.fechaHoraFin is None


    def setFechaFin(self, fechaFin):
        self.fechaHoraFin = fechaFin
