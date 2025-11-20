from ClasesEntidad.Estado import Estado

class Rechazado(Estado):
    def __init__(self, ambito):
        super().__init__(ambito)
        self.nombreEstado = "Rechazado"


    def esRechazado(self):
        return self.nombreEstado.lower() == "rechazado"