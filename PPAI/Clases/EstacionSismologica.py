class EstacionSismologica:
    def __init__(self, nombre):
        self._nombre = nombre
        #tiene un monton de atributos

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre