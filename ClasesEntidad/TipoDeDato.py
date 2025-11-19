class TipoDeDato:
    def __init__(self, denominacion, nombreUnidadMedida, valorUmbral):
        self.denominacion = denominacion
        self.nombreUnidadMedida = nombreUnidadMedida
        self.valorUmbral = valorUmbral


    def getDenominacion(self):
        return self.denominacion


    def getNombreUnidadMedida(self):
        return self.nombreUnidadMedida


    def esTuDenominacion(self, denominacion):
        return denominacion == self.denominacion
