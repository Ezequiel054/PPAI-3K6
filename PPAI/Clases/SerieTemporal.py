class SerieTemporal:
    def __init__(self, condicion_alarma, fecha_inicio_registro, fecha_registro, frecuencia_muestreo):
        self._condicion_alarma = condicion_alarma
        self._fecha_inicio_registro_muestras = fecha_inicio_registro
        self._fecha_hora_registro = fecha_registro
        self._frecuencia_muestreo = frecuencia_muestreo
        self._muestras = []  # lista de MuestraSismica

    def obtenerMuestrasSismicas(self):
        return self._muestras

    def agregarMuestraSismica(self, muestra):
        self._muestras.append(muestra)

    def getDatos(self):
        return {
            "condicionAlarma": self._condicion_alarma,
            "fechaInicioRegistroMuestras": self._fecha_inicio_registro_muestras,
            "fechaHoraRegistro": self._fecha_hora_registro,
            "frecuenciaMuestreo": self._frecuencia_muestreo,
            "cantidadMuestras": len(self._muestras)
        }

    ## revisar metodos de arriba
    def getDatos(self):
            self.obtenerMuestrasSismicas()

    def obtenerMuestrasSismicas(self):
        # aca habria que crear datosMuestrales como lista o no hace falta?
        for ms in self._muestras:
            datosMuestrales = ms.getDatos()

        return datosMuestrales


    def getCondicionAlarma(self):
        return self._condicion_alarma

    def setCondicionAlarma(self, condicion):
        self._condicion_alarma = condicion

    def getFechaInicioRegistroMuestras(self):
        return self._fecha_inicio_registro_muestras

    def setFechaInicioRegistroMuestras(self, fecha):
        self._fecha_inicio_registro_muestras = fecha

    def getFechaHoraRegistro(self):
        return self._fecha_hora_registro

    def setFechaHoraRegistro(self, fecha):
        self._fecha_hora_registro = fecha

    def getFrecuenciaMuestreo(self):
        return self._frecuencia_muestreo

    def setFrecuenciaMuestreo(self, frecuencia):
        self._frecuencia_muestreo = frecuencia
