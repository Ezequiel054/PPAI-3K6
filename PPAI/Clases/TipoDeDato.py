class TipoDeDato:
    def __init__(self, denominacion, nombre_unidad_medida, valor_umbral):
        self._denominacion = denominacion
        self._nombre_unidad_medida = nombre_unidad_medida
        self._valor_umbral = valor_umbral

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

    def getValorUmbral(self):
        return self._valor_umbral

    def setValorUmbral(self, valor):
        self._valor_umbral = valor
