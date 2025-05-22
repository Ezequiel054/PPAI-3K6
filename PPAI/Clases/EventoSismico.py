from Clases.CambioEstado import CambioEstado
from Clases.Estado import Estado

class EventoSismico:
    # def __new__(cls, fechaHoraFin,FechaHoraOcurrencia,latitudEpicentro,latitudHipocentro,longitudEpicentro,longitudHipocentro,valorMagnitud,estadoActual):
    #     instancia = super().__new__(cls)
    #     instancia.fechaHoraFin = fechaHoraFin
    #     instancia.FechaHoraOcurrencia = FechaHoraOcurrencia
    #     instancia.latitudEpicentro = latitudEpicentro
    #     instancia.latitudHipocentro = latitudHipocentro
    #     instancia.longitudEpicentro = longitudEpicentro
    #     instancia.longitudHipocentro = longitudHipocentro
    #     instancia.valorMagnitud = valorMagnitud
    #     instancia.estadoActual = estadoActual
    #     return instancia
    
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
        return self.estadoActual.esAutodetectado()
    
    def obtenerDatosPrincipales(self):
        datos_evento = {
        "fechaHoraOcurrencia": self.get_FechaHoraOcurrencia(),
        "latitudEpicentro": self.get_latitudEpicentro(),
        "longitudHipocentro": self.get_longitudHipocentro(),
        "valorMagnitud": self.get_valorMagnitud(),
        "longitudEpicentro": self.get_longitudEpicentro(),
        "latitudHipocentro": self.get_latitudHipocentro()}
        return datos_evento

    def bloquearEnRevision(self, fechaActual, estadoBloqueadoEnRevision,usuarioLogueado):
        cambioEstadoActual = self.buscarEstadoActual()
        cambioEstadoActual.setFechaHoraFin(fechaActual)

        self.setEstadoActual(estadoBloqueadoEnRevision)
        cambioEstadoBloqueadoEnRevision = self.crearCambioEstado(fechaActual, estadoBloqueadoEnRevision,usuarioLogueado)
        self.cambioEstado.append(cambioEstadoBloqueadoEnRevision)

    def buscarEstadoActual(self):
        for ce in self.cambioEstado:
            if ce.esEstadoActual():
                return ce
                
        
    def setEstadoActual(self, estado):
        self.estadoActual = estado

    def crearCambioEstado(self, nuevoEstado, fechaHoraInicio, usuarioLogueado):
        return CambioEstado(nuevoEstado,fechaHoraInicio, usuarioLogueado)
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

    def rechazar(self,fechaActual,estadoRechazado):
        cambioEstadoActual = self.buscarEstadoActual()
        cambioEstadoActual.setFechaHoraFin(fechaActual)

        self.setEstadoActual(estadoRechazado)
        cambioEstadoRechazado = self.crearCambioEstado(fechaActual, estadoRechazado)
        self.cambioEstado.append(cambioEstadoRechazado)


    """ 
        A5: El AS no completa los datos mínimos
        A6: Si la opción seleccionada es Confirmar evento, se actualiza el estado del evento sísmico a confirmado,
            registrando la fecha y hora actual como fecha de confirmación. y el AS logueado como responsable
        A7: Si la opción seleccionada es Solicitar revisión a experto, se actualiza el estado del evento sísmico a derivado a experto, 
            registrando la fecha y hora actual, y el AS logueado
    """

    def confirmar(self,fechaActual,estadoConfirmado):
        cambioEstadoActual = self.buscarEstadoActual()
        cambioEstadoActual.setFechaHoraFin(fechaActual)

        self.setEstadoActual(estadoConfirmado)
        cambioEstadoConfirmado = self.crearCambioEstado(fechaActual, estadoConfirmado)
        self.cambioEstado.append(cambioEstadoConfirmado)

    def derivarARevision(self,fechaActual,estadoDerivadoARevision):
        cambioEstadoActual = self.buscarEstadoActual()
        cambioEstadoActual.setFechaHoraFin(fechaActual)

        self.setEstadoActual(estadoDerivadoARevision)
        cambioEstadoDerivadoARevision = self.crearCambioEstado(fechaActual, estadoDerivadoARevision)
        self.cambioEstado.append(cambioEstadoDerivadoARevision)


    def modificarDatos(self, magnitud,alcance,origen):
        self.alcanceSismo.setNombre(alcance)
        self.origenGeneracion.setNombre(origen)
        self.set_valorMagnitud(magnitud)