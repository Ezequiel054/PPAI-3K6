class MuestraSismica:
    def __init__(self, fechaHoraMuestra, detallesMuestrasSismica):
        self.fechaHoraMuestra = fechaHoraMuestra
        self.detallesMuestrasSismica = []
        self.detallesMuestrasSismica = detallesMuestrasSismica

    def crearDetalleMuestra(self, detalle):
        self._detalles.append(detalle)

    def getDatos(self):
        return {
            "fechaHoraMuestra": self.fechaHoraMuestra,
            "detalles": [d.getDatos() for d in self._detalles]
        }

    def getFechaHoraMuestra(self):
        return self.fechaHoraMuestra

    def setFechaHoraMuestra(self, fecha):
        self.fechaHoraMuestra = fecha

    def getDetalles(self):
        return self._detalles

    ## modifco desde aca
    def getDatos(self):
        fechaHoraMuestra = self.getFechaHoraMuestra()
        datosMuestrales = self.obtenerDetalleMuestra()
        
        return fechaHoraMuestra, datosMuestrales

    ## este metodo no esta en la secuncia, seria un self, revisar
    def obtenerDetalleMuestra(self):
        datosMuestrales = []
        for dm in self.detallesMuestrasSismica:

            datosMuestra = dm.getDatos()
            ## Denominacion, valor, nombreUnidadMedida
            ## Velocidad de onda,7,Km/seg 
            datosMuestrales.append(datosMuestra)
        
        return datosMuestrales
