class Empleado:
    def __init__(self, nombre, apellido, id=None):
        self.nombre = nombre
        self.apellido = apellido
        self.id = id


    def getNombreUsuario(self):
        return self.nombre

