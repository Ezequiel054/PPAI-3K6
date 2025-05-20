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
                 cambioEstado, alcanceSismo, origenGeneracion, clasificacion,serieTemporal ):
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
        self.buscarEstadoActual(fechaActual)
        self.setEstadoActual(bloqueadoEnRevision)
        nuevoCambioEstado = self.crearCambioEstado(fechaActual, bloqueadoEnRevision)
        self.cambioEstado.append(nuevoCambioEstado)

    def buscarEstadoActual(self, fechaHoraFin):
        for ce in self.cambioEstado:
            if ce.esEstadoActual():
                ce.setFechaHoraFin(fechaHoraFin)
                # revisar esta parte, setFechHoraFin debe estar por fuera del loop?
                #  en ese caso esEstadoActual debe retornar puntero a ese estado
        

    def setEstadoActual(self, estado):
        self.estadoActual = estado

    def crearCambioEstado(self, fechaHoraInicio, bloqueadoEnRevision):
        return CambioEstado(bloqueadoEnRevision,fechaHoraInicio, None)
        ## revisar el None, se pasa como parametro al crear un nuevo CE?

    def getDatosRestantes(self):
        
        alcance = self.alcanceSismo.getNombre()
        clasificacion = self.clasificacion.getNombre()
        origenGeneracion = self.origenGeneracion.getNombre()

        return alcance, clasificacion, origenGeneracion

    def obtenerDatosSeriesTemporal(self):
        
        for st in self.serieTemporal:
            st.getDatos()

