class Usuario:
    def __init__(self, nombreUsuario, password, empleado):
        self.nombreUsuario = nombreUsuario
        self.password = password
        self.empleado = empleado


    def getEmpleado(self):
        return self.empleado