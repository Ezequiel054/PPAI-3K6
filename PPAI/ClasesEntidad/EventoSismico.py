from ClasesEntidad.CambioEstado import CambioEstado

class EventoSismico:
    def __init__(self, fechHorOcurr, fechHorFin, latEpicentro, latHipocentro,
                 longHipocentro, longEpicentro, valorMagnitud,
                 clasif, origen, alcance, serieTemp, estAct, cambioEst):
        # Valores
        self.fechaHoraOcurrencia = fechHorOcurr
        self.fechaHoraFin = fechHorFin
        self.latitudEpicentro = latEpicentro
        self.latitudHipocentro = latHipocentro
        self.longitudEpicentro = longEpicentro
        self.longitudHipocentro = longHipocentro
        self.valorMagnitud = valorMagnitud

        # Objetos
        self.clasificacion = clasif
        self.origenGeneracion = origen
        self.alcanceSismo = alcance
        self.serieTemporal = serieTemp
        self.estadoActual = estAct
        self.cambioEstado = cambioEst


    def esAutodetectado(self):
        return self.estadoActual.esAutodetectado()


    def obtenerDatosPrincipales(self):
        datosEvento = {
            "fechaHoraOcurrencia": self.fechaHoraOcurrencia,
            "latitudEpicentro": self.latitudEpicentro,
            "longitudEpicentro": self.longitudEpicentro,
            "latitudHipocentro": self.latitudHipocentro,
            "longitudHipocentro": self.longitudHipocentro,
            "valorMagnitud": self.valorMagnitud
        }

        return datosEvento


    def bloquearEnRevision(self, estadoBloqueado, fecha, empleado):
        self.buscarEstadoActual(fecha)
        self.setEstadoActual(estadoBloqueado)
        self.cambioEstado.append(self.crearCambioEstado(fecha, estadoBloqueado, empleado))


    def buscarEstadoActual(self, fechaFin):
        for cambioEst in self.cambioEstado:
            if cambioEst.esEstadoActual():
                cambioEst.setFechaHoraFin = fechaFin


    def setEstadoActual(self, estado):
        self.estadoActual = estado


    def crearCambioEstado(self, fecha, estado, empleado):
        cambioEstado = CambioEstado(fechaHoraInicio= fecha, fechaHoraFin=None,
                                    estado=estado, responsableInspeccion=empleado)
        return cambioEstado


    def getDatosRestantes(self):
        datos = [self.alcanceSismo.getNombre(),
                 self.clasificacion.getNombre(),
                 self.origenGeneracion.getNombre()]
        return datos


    def obtenerDatosSerieTemporal(self):
        series = []
        for ser in self.serieTemporal:
            series.append(ser.getDatos())
        return series


    def rechazar(self, estadoRechazado, fecha, empleado):
        self.buscarEstadoActual(fecha)
        self.setEstadoActual(estadoRechazado)
        self.cambioEstado.append(self.crearCambioEstado(fecha, estadoRechazado, empleado))


    def confirmar(self, estadoConfirmado, fecha, empleado):
        self.buscarEstadoActual(fecha)
        self.setEstadoActual(estadoConfirmado)
        self.cambioEstado.append(self.crearCambioEstado(fecha, estadoConfirmado, empleado))