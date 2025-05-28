class ClasificacionSismo:
    def __init__(self, nom, kmDesde, kmHasta):
        self.nombre = nom
        self.kmProfundidadDesde = kmDesde
        self.kmProfundidadHasta = kmHasta


    def getNombre(self):
        return self.nombre
