class Sesion:
    def __init__(self, fechaHoraDesde, fechaHoraHasta, usuario):
        self.fechaHoraDesde = fechaHoraDesde
        self.fechaHoraHasta = fechaHoraHasta
        self.usuario = usuario


    def getEmpleado(self):
        return self.usuario.getEmpleado()