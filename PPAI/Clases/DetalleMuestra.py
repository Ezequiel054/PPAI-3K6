class DetalleMuestra:
    def __init__(self, valor, tipo_de_dato):
        self._valor = valor
        self._tipo_de_dato = tipo_de_dato  # instancia de TipoDeDato

    def getDatos(self):
        return {"valor": self._valor, "tipoDeDato": self._tipo_de_dato.getDenominacion()}

    def getValor(self):
        return self._valor

    def setValor(self, valor):
        self._valor = valor

    def getTipoDeDato(self):
        return self._tipo_de_dato

    def setTipoDeDato(self, tipo_de_dato):
        self._tipo_de_dato = tipo_de_dato
