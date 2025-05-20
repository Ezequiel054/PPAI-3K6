class DetalleMuestra:
    def __init__(self, valor, tipoDato):
        self.valor = valor
        self.tipoDato = tipoDato  # 1 sola instancia de tipoDato

    def getDatos(self):
        return self.tipoDato.getDenominacion(), self.getValor(), self.tipoDato.getNombreUnidadMedida()

    def getValor(self):
        return self.valor

    def setValor(self, valor):
        self.valor = valor

    def getTipoDeDato(self):
        return self.tipoDato

    def setTipoDeDato(self, tipoDato):
        self.tipoDato = tipoDato
