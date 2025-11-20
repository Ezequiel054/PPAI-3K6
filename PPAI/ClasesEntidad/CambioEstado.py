# no imports a la capa de persistencia desde las entidades

class CambioEstado:
    def __init__(self, fechaHoraInicio, fechaHoraFin, estado, responsableInspeccion):
        self.fechaHoraInicio = fechaHoraInicio
        self.fechaHoraFin = fechaHoraFin
        self.estado = estado
        self.responsableInspeccion = responsableInspeccion

    def __str__(self):
        return f"\nCambioEstado({self.fechaHoraInicio}, {self.fechaHoraFin}, {self.estado.nombreEstado}, {self.responsableInspeccion.nombre})\n"

    def esEstadoActual(self):
        return self.fechaHoraFin is None

    def setFechaFin(self, fechaFin):
        # Solo actualiza el objeto en memoria; la capa de persistencia debe encargarse de guardar este cambio.
        self.fechaHoraFin = fechaFin

