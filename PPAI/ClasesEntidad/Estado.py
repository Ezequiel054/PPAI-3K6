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

