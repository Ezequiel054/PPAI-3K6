from ClasesEntidad.Estado import Estado

class Rechazado(Estado):
    def __init__(self):
        super().__init__()
        self.nombreEstado = "Rechazado"


    def esRechazado(self):
        return self.nombreEstado.lower() == "rechazado"