class DetalleMuestraSismica:
    def __init__(self, valor, tipoDeDato):
        self.valor = valor
        self.tipoDeDato = tipoDeDato


    def getDatos(self):
        return [self.getValor(), self.tipoDeDato.getDenominacion(), self.tipoDeDato.getNombreUnidadMedida()]


    def getValor(self):
        return self.valor
