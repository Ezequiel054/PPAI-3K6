class MuestraSismica:
    def __init__(self, fecha_hora_muestra):
        self._fecha_hora_muestra = fecha_hora_muestra
        self._detalles = []  # lista de DetalleMuestra

    def crearDetalleMuestra(self, detalle):
        self._detalles.append(detalle)

    def getDatos(self):
        return {
            "fechaHoraMuestra": self._fecha_hora_muestra,
            "detalles": [d.getDatos() for d in self._detalles]
        }

    def getFechaHoraMuestra(self):
        return self._fecha_hora_muestra

    def setFechaHoraMuestra(self, fecha):
        self._fecha_hora_muestra = fecha

    def getDetalles(self):
        return self._detalles
