class Estado:
    def __init__(self, ambito, nombreEstado):
        self.ambito = ambito
        self.nombreEstado = nombreEstado


    def esAutodetectado(self):
        return self.nombreEstado.lower() == "autodetectado"


    def esBloqueadoEnRevision(self):
        return self.nombreEstado.lower() == "bloqueado en revision"


    def esRechazado(self):
        return self.nombreEstado.lower() == "rechazado"


    def esAmbitoEventoSismico(self):
        return self.ambito.lower() == "evento sismico"
