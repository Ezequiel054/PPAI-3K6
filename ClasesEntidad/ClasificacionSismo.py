class ClasificacionSismo:
    def __init__(self, nombre, kmDesde, kmHasta):
        self.nombre = nombre
        self.kmProfundidadDesde = kmDesde
        self.kmProfundidadHasta = kmHasta

    def __str__(self):
        return f"ClasificacionSismo(nombre={self.nombre}, kmProfundidadDesde={self.kmProfundidadDesde}, kmProfundidadHasta={self.kmProfundidadHasta})"

    def getNombre(self):
        return self.nombre
