class Sismografo:
    def __init__(self, estacionSismologica, seriesTemporales): 
        self._estacionSismologica = estacionSismologica
        self.seriesTemporales = seriesTemporales
  
    def getEstacionSismologica(self):
        return self._estacionSismologica

    def setEstacionSismologica(self, estacionSismologica):
        self._estacionSismologica = estacionSismologica
    
    def getSeriesTemporales(self):
        return self.seriesTemporales

    def setSeriesTemporales(self, seriesTemporales):
        self.seriesTemporales = seriesTemporales
