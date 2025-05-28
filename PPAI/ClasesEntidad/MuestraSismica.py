class MuestraSismica:
    def __init__(self, fechaHoraMuestra, detalleMuestraSismica):
        self.fechaHoraMuestra = fechaHoraMuestra
        self.detalleMuestraSismica = detalleMuestraSismica


    def getDatos(self):
        fechaHoraMuestra = self.getFechaHoraMuestra()
        detalles = []
        for det in self.detalleMuestraSismica:
            detalles.append(det.getDatos())
        return [fechaHoraMuestra, detalles]


    def getFechaHoraMuestra(self):
        return self.fechaHoraMuestra
