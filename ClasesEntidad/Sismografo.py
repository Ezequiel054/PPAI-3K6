class Sismografo:
    def __init__(self, fechaAdquisicion, identificadorSismografo, nroSerie,
                 estacionSismologica, serieTemporal):
        self.fechaAdquisicion = fechaAdquisicion
        self.identificadorSismografo = identificadorSismografo
        self.nroSerie = nroSerie
        self.estacionSismologica = estacionSismologica
        self.serieTemporal = serieTemporal


    def sosDeSerieTemporal(self, serie):
        return serie == self.serieTemporal


    def getEstacionSismologica(self):
        return self.estacionSismologica.getNombre()


    def getSerieTemporal(self):
        return self.serieTemporal
