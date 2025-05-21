class Sesion:
    def __init__(self, usuario=None):
        self.usuario = usuario

    def getEmpleado(self):
        return self.usuario.getEmpleado()
