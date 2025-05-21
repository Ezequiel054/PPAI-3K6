from Clases.CambioEstado import CambioEstado
class EventoSismico:
    def __new__(cls, fechaHoraFin,FechaHoraOcurrencia,latitudEpicentro,latitudHipocentro,longitudEpicentro,longitudHipocentro,valorMagnitud,estadoActual):
        instancia = super().__new__(cls)
        instancia.fechaHoraFin = fechaHoraFin
        instancia.FechaHoraOcurrencia = FechaHoraOcurrencia
        instancia.latitudEpicentro = latitudEpicentro
        instancia.latitudHipocentro = latitudHipocentro
        instancia.longitudEpicentro = longitudEpicentro
        instancia.longitudHipocentro = longitudHipocentro
        instancia.valorMagnitud = valorMagnitud
        instancia.estadoActual = estadoActual
        return instancia
    
    def __init__(self,fechaHoraFin,FechaHoraOcurrencia,latitudEpicentro,latitudHipocentro,longitudEpicentro,
                 longitudHipocentro, valorMagnitud, estadoActual,
                 cambioEstado, alcanceSismo, origenGeneracion, clasificacion,serieTemporal):
        self.fechaHoraFin = fechaHoraFin
        self.FechaHoraOcurrencia = FechaHoraOcurrencia
        self.latitudEpicentro = latitudEpicentro
        self.latitudHipocentro = latitudHipocentro
        self.longitudEpicentro = longitudEpicentro
        self.longitudHipocentro = longitudHipocentro
        self.valorMagnitud = valorMagnitud
        self.estadoActual = estadoActual
        
        ## revisar estos atributos
        self.cambioEstado = []
        self.cambioEstado = cambioEstado
        self.origenGeneracion = origenGeneracion
        self.alcanceSismo = alcanceSismo
        self.clasificacion = clasificacion

        self.serieTemporal = []
        self.serieTemporal = serieTemporal

      


    def get_fechaHoraFin(self):
        return self.fechaHoraFin

    def set_fechaHoraFin(self, fechaHoraFin):
        self.fechaHoraFin = fechaHoraFin

    def get_FechaHoraOcurrencia(self):
        return self.FechaHoraOcurrencia

    def set_FechaHoraOcurrencia(self, FechaHoraOcurrencia):
        self.FechaHoraOcurrencia = FechaHoraOcurrencia

    def get_latitudEpicentro(self):
        return self.latitudEpicentro

    def set_latitudEpicentro(self, latitudEpicentro):
        self.latitudEpicentro = latitudEpicentro

    def get_latitudHipocentro(self):
        return self.latitudHipocentro

    def set_latitudHipocentro(self, latitudHipocentro):
        self.latitudHipocentro = latitudHipocentro

    def get_longitudEpicentro(self):
        return self.longitudEpicentro

    def set_longitudEpicentro(self, longitudEpicentro):
        self.longitudEpicentro = longitudEpicentro

    def get_longitudHipocentro(self):
        return self.longitudHipocentro

    def set_longitudHipocentro(self, longitudHipocentro):
        self.longitudHipocentro = longitudHipocentro

    def get_valorMagnitud(self):
        return self.valorMagnitud

    def set_valorMagnitud(self, valorMagnitud):
        self.valorMagnitud = valorMagnitud


    def esAutodetectado(self):
        return self.estadoActual.esAutoDetectado()
    
    def obtenerDatosPrincipales(self):
        datos_evento = {
        "FechaHoraOcurrencia": self.get_FechaHoraOcurrencia(),
        "LatitudEpicentro": self.get_latitudEpicentro(),
        "LongitudHipocentro": self.get_longitudHipocentro(),
        "ValorMagnitud": self.get_valorMagnitud(),
        "LongitudEpicentro": self.get_longitudEpicentro(),
        "LatitudHipocentro": self.get_latitudHipocentro()}
        return datos_evento

    def bloquearEnRevision(self, fechaActual, bloqueadoEnRevision):
        cambioEstadoActual = self.buscarEstadoActual()
        cambioEstadoActual.setFechaHoraFin(fechaActual)

        self.setEstadoActual(bloqueadoEnRevision)
        bloqueadoEnRevision = self.crearCambioEstado(fechaActual, bloqueadoEnRevision)
        self.cambioEstado.append(bloqueadoEnRevision)

    def buscarEstadoActual(self):
        for ce in self.cambioEstado:
            if ce.esEstadoActual():
                return ce
                
        
    def setEstadoActual(self, estado):
        self.estadoActual = estado

    def crearCambioEstado(self, fechaHoraInicio, nuevoEstado):
        return CambioEstado(nuevoEstado,fechaHoraInicio)
        ## agegar el empleado al CE

    def getDatosRestantes(self):
        
        alcance = self.alcanceSismo.getNombre()
        clasificacion = self.clasificacion.getNombre()
        origenGeneracion = self.origenGeneracion.getNombre()

        return alcance, clasificacion, origenGeneracion

    def obtenerDatosSeriesTemporal(self):
        
        datosSeriesTemporalesPorEstacion = []
        for st in self.serieTemporal:
            datosSeriesTemporal = st.getDatos()
            ## Estacion Sismologica,[ [FechaHoraMuestra ,Denominacion, valor, nombreUnidadMedida],[FechaHoraMuestra ,Denominacion, valor, nombreUnidadMedida] ]

            datosSeriesTemporalesPorEstacion.append(datosSeriesTemporal)

        return datosSeriesTemporalesPorEstacion

    def rechazar(self,fechaActual,rechazado):
        cambioEstadoActual = self.buscarEstadoActual()
        cambioEstadoActual.setFechaHoraFin(fechaActual)

        self.setEstadoActual(rechazado)
        rechazado = self.crearCambioEstado(fechaActual, rechazado)
        self.cambioEstado.append(rechazado)
