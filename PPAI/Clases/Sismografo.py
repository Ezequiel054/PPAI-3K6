class Sismografo:
    def __init__(self, estacionSismologica, seriesTemporales): #def __init__(self, estacionSismologica, fechaAdquisicion, identificadorSismografo, nroSerie):
        self._estacionSismologica = estacionSismologica
        self.seriesTemporales = seriesTemporales
        #self._fechaAdquisicion = fechaAdquisicion
        #self._identificadorSismografo = identificadorSismografo
        #self._nroSerie = nroSerie

    def getEstacionSismologica(self):
        return self._estacionSismologica

    def setEstacionSismologica(self, estacionSismologica):
        self._estacionSismologica = estacionSismologica
    
    def getSeriesTemporales(self):
        return self.seriesTemporales

    def setSeriesTemporales(self, seriesTemporales):
        self.seriesTemporales = seriesTemporales

    def sosDeSerietemporal(self): ##########
        for serieTemporal in self.seriesTemporales:
            
            if self.seriesTemporales:
                pass
        
        nombreEstacionSismologica = self.estacionSismologica.getNombre()
        return nombreEstacionSismologica
        