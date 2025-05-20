from datetime import datetime

class CambioEstado:
    def __init__(self, estado, fecha_hora_inicio, fecha_hora_fin=None):
        self._estado = estado  # Instancia de la clase Estado
        self._fecha_hora_inicio = fecha_hora_inicio
        self._fecha_hora_fin = fecha_hora_fin

    def getEstado(self):
        return self._estado

    def setEstado(self, estado):
        self._estado = estado

    def getFechaHoraInicio(self):
        return self._fecha_hora_inicio

    def setFechaHoraInicio(self, fecha_hora_inicio):
        self._fecha_hora_inicio = fecha_hora_inicio

    def getFechaHoraFin(self):
        return self._fecha_hora_fin

    def setFechaHoraFin(self, fecha_hora_fin):
        self._fecha_hora_fin = fecha_hora_fin

    def esEstadoActual(self):
        return self._fecha_hora_fin is None
