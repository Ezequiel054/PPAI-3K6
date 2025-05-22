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



    def esAmbitoEventoSismico(self):
        return self._ambito.lower() == "evento sismico"


######## aca van

    def esAutodetectado(self):
        return self._nombre_estado == "Autodetectado"
    def esBloqueadoEnRevision(self):
        return self._nombre_estado == "Bloqueado en revision"

    def esRechazado(self):
        return self._nombre_estado == "Rechazado"

    def esDerivadoAExperto(self):
        return self._nombre_estado == "Derivado a experto"
    
    def esConfirmado(self):
        return self._nombre_estado == "Confirmado"
