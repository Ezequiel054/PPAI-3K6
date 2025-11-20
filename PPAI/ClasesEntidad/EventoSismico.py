from ClasesEntidad.CambioEstado import CambioEstado

class EventoSismico:
    def __init__(self, fechHorOcurr, fechHorFin, latEpicentro, latHipocentro,
                 longHipocentro, longEpicentro, valorMagnitud,
                 clasif, origen, alcance, serieTemp, estAct, cambiosEst):
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
        self.cambiosEstado = cambiosEst


    # def __str__(self):
    #    return f"EventoSismico({self.fechaHoraOcurrencia}, {self.latitudEpicentro}, {self.longitudEpicentro}, {self.valorMagnitud})"
    
    # def __str__(self):
    #    atributos = ", ".join(f"{k}={v}" for k, v in self.__dict__.items())
    #    return f"EventoSismico({atributos})"

    def __str__(self):
        atributos = []
        for k, v in self.__dict__.items():
            if k == "cambiosEstado" and isinstance(v, list):
                # Convertir cada cambio a string
                cambios = ", ".join(str(c) for c in v)
                atributos.append(f"{k}=[{cambios}]")
            else:
                atributos.append(f"{k}={v}")
        
        return "EventoSismico(" + ", ".join(atributos) + ")"


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


    def bloquearEnRevision(self, fecha, empleado):
        self.estadoActual.bloquearEnRevision(fecha, empleado, self.cambiosEstado, self)
        # self.buscarEstadoActual(fecha)
        # self.setEstadoActual(estadoBloqueado)
        # self.cambioEstado.append(self.crearCambioEstado(fecha, estadoBloqueado, empleado))

        # self.estadoActual.bloquearEnRevision(fecha,empleado,self.cambioEstado,self)


    def agregarCambioEstado(self,nuevoCambioEstado):
        self.cambiosEstado.append(nuevoCambioEstado)
        for c in self.cambiosEstado:
            print(c)



    # def buscarEstadoActual(self, fechaFin):
    #     for cambioEst in self.cambiosEstado:
    #         if cambioEst.esEstadoActual():
    #             cambioEst.setFechaHoraFin = fechaFin


    def setEstadoActual(self, estado):
        # Actualiza solo en memoria; la capa de persistencia (DAO/repositorio) debe encargarse de persistir.
        self.estadoActual = estado


    # def crearCambioEstado(self, fecha, estado, empleado):
    #     cambioEstado = CambioEstado(fechaHoraInicio= fecha, fechaHoraFin=None,
    #                                 estado=estado, responsableInspeccion=empleado)
    #     return cambioEstado


    def getDatosRestantes(self):
        datos = [self.alcanceSismo.getNombre(),
                 self.clasificacion.getNombre(),
                 self.origenGeneracion.getNombre()]
        return datos


    def obtenerDatosSerieTemporal(self):
        # Devuelve array con las series, y datos a presentar de cada serie
        series = []
        for ser in self.serieTemporal:
            series.append([ser, ser.getDatos()]) # Cada elemento de array es: [serie, datosAPresentar]
        return series


    # def rechazar(self, estadoRechazado, fecha, empleado):
    #     self.buscarEstadoActual(fecha)
    #     self.setEstadoActual(estadoRechazado)
    #     self.cambiosEstado.append(self.crearCambioEstado(fecha, estadoRechazado, empleado))


    # def confirmar(self, estadoConfirmado, fecha, empleado):
    #     self.buscarEstadoActual(fecha)
    #     self.setEstadoActual(estadoConfirmado)
    #     self.cambiosEstado.append(self.crearCambioEstado(fecha, estadoConfirmado, empleado))



    def rechazarEvento(self,fecha,empleado):
        self.estadoActual.rechazar(fecha, empleado, self.cambiosEstado, self)

