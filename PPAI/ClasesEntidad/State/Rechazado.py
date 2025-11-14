from ClasesEntidad.Estado import Estado

class Rechazado(Estado):
    def __init__(self, ambito, id=4):
        super().__init__(ambito, id)
        self.nombreEstado = "Rechazado"


    def esRechazado(self):
        return self.nombreEstado.lower() == "rechazado"