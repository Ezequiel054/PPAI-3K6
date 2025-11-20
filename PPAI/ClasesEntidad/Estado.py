from abc import ABC, abstractmethod

class Estado(ABC):
    def __init__(self, ambito, id=None):
        self.ambito = ambito
        self.nombreEstado = ""
        # no almacenar ni exponer nada relacionado a BD en la entidad

    def esAutodetectado(self):
        return False

    def esBloqueadoEnRevision(self):
        return False
    
    def esRechazado(self):
        return False
    
    def esAmbitoEventoSismico(self):
        print("Este estado no puede recibir esa operacion")
    
    def esConfirmado(self):
        print("Este estado no puede recibir esa operacion")

