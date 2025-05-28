class SerieTemporal:
    def __init__(self, condicionAlarma, fechaHoraInicioRegistroMuestras, fechaHoraRegistro,
                 frecuenciaMuestreo, muestraSismica):
        self.condicionAlarma = condicionAlarma
        self.fechaHoraInicioRegistroMuestras = fechaHoraInicioRegistroMuestras
        self.fechaHoraRegistro = fechaHoraRegistro
        self.frecuenciaMuestreo = frecuenciaMuestreo
        self.muestraSismica = muestraSismica


    def getDatos(self):
        serieDatos = [self.condicionAlarma, self.fechaHoraInicioRegistroMuestras, self.frecuenciaMuestreo]
        muestras = []
        for m in self.muestraSismica:
            muestras.append(self.obtenerMuestrasSismicas(m))
        return [serieDatos, muestras]


    def obtenerMuestrasSismicas(self, muestra):
        return muestra.getDatos()
