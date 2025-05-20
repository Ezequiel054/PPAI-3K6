class ClasificacionSismo:
    def __init__(self, km_profundidad_desde, km_profundidad_hasta, nombre):
        self._km_profundidad_desde = km_profundidad_desde
        self._km_profundidad_hasta = km_profundidad_hasta
        self._nombre = nombre

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getKmProfundidadDesde(self):
        return self._km_profundidad_desde

    def setKmProfundidadDesde(self, valor):
        self._km_profundidad_desde = valor

    def getKmProfundidadHasta(self):
        return self._km_profundidad_hasta

    def setKmProfundidadHasta(self, valor):
        self._km_profundidad_hasta = valor
