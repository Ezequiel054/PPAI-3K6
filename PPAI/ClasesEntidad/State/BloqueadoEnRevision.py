from ClasesEntidad.Estado import Estado

class BloqueadoEnRevision(Estado):
    def __init__(self, ambito):
        super().__init__(ambito)
    
