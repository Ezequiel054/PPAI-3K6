class TipoDeDato:
    def __init__(self, denominacion, nombre_unidad_medida):
        self._denominacion = denominacion
        self._nombre_unidad_medida = nombre_unidad_medida
    
    def esTuDenominacion(self, denominacion):
        return self._denominacion == denominacion

    def getDenominacion(self):
        return self._denominacion

    def setDenominacion(self, denominacion):
        self._denominacion = denominacion

    def getNombreUnidadMedida(self):
        return self._nombre_unidad_medida

    def setNombreUnidadMedida(self, unidad):
        self._nombre_unidad_medida = unidad
