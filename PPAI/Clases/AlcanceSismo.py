class AlcanceSismo:
    def __init__(self, descripcion, nombre):
        self._descripcion = descripcion
        self._nombre = nombre

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getDescripcion(self):
        return self._descripcion

    def setDescripcion(self, descripcion):
        self._descripcion = descripcion
