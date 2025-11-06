from abc import ABC, abstractmethod

class Estado(ABC):
    def __init__(self, ambito):
        self.ambito = ambito
        self.nombreEstado = ""

    def esAutodetectado(self):
        print("Este estado no puede recibir esa operacion")

    def esBloqueadoEnRevision(self):
        print("Este estado no puede recibir esa operacion")
    
    def esRechazado(self):
        print("Este estado no puede recibir esa operacion")
    
    def esAmbitoEventoSismico(self):
        print("Este estado no puede recibir esa operacion")
    
    def esConfirmado(self):
        print("Este estado no puede recibir esa operacion")

    # def esAutodetectado(self):
    #     return self.nombreEstado.lower() == "autodetectado"

    # def esBloqueadoEnRevision(self):
    #     return self.nombreEstado.lower() == "bloqueado en revision"


    # def esRechazado(self):
    #     return self.nombreEstado.lower() == "rechazado"


    # def esAmbitoEventoSismico(self):
    #     return self.ambito.lower() == "evento sismico"


    # # Alternativo = Confirmar Evento
    # def esConfirmado(self):
    #     return self.nombreEstado.lower() == "confirmado"
