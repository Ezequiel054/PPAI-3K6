class Estado:
    def __init__(self, ambito, nombre_estado):
        self._ambito = ambito
        self._nombre_estado = nombre_estado

    def getAmbito(self):
        return self._ambito

    def setAmbito(self, ambito):
        self._ambito = ambito

    def getNombreEstado(self):
        return self._nombre_estado

    def setNombreEstado(self, nombre_estado):
        self._nombre_estado = nombre_estado

    def esAutodetectado(self):
        return self._nombre_estado.lower() == "autodetectado"

    def esAmbitoEventoSismico(self):
        return self._ambito.lower() == "evento sismico"

    def esBloqueadoEnRevision(self):
        return self._nombre_estado.lower() == "bloqueado en revisión"

    def esRechazado(self):
        return self._nombre_estado.lower() == "rechazado"
