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
    
    def __init__(self,fechaHoraFin,FechaHoraOcurrencia,latitudEpicentro,latitudHipocentro,longitudEpicentro,longitudHipocentro,valorMagnitud,estadoActual):
        self.fechaHoraFin = fechaHoraFin
        self.FechaHoraOcurrencia = FechaHoraOcurrencia
        self.latitudEpicentro = latitudEpicentro
        self.latitudHipocentro = latitudHipocentro
        self.longitudEpicentro = longitudEpicentro
        self.longitudHipocentro = longitudHipocentro
        self.valorMagnitud = valorMagnitud
        self.estadoActual = estadoActual

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


    # Esta función obtiene las reseñas de un vino en un período de tiempo específico realizadas por un sommelier en particular.
    # Si no hay reseñas que cumplan con los criterios, retorna False y una lista vacía.
    # Si hay reseñas que cumplan con los criterios, retorna True y la lista de reseñas.

    
    # Esta función obtiene y retorna el nombre de la bodega asociada a la instancia actual.
    def esAutodetectado(self):
        return self.estadoActual.esAutoDetectado()
    
    # Esta función obtiene y retorna una lista de descripciones de los varietales de un vino.
    def obtenerDatosPrincipales(self):
        datos_evento = {
        "FechaHoraOcurrencia": self.get_FechaHoraOcurrencia(),
        "LatitudEpicentro": self.get_latitudEpicentro(),
        "LongitudHipocentro": self.get_longitudHipocentro(),
        "ValorMagnitud": self.get_valorMagnitud(),
        "LongitudEpicentro": self.get_longitudEpicentro(),
        "LatitudHipocentro": self.get_latitudHipocentro()}
        return datos_evento

    # Esta función calcula y retorna el puntaje promedio de una lista de puntajes.
    # La lista de puntajes puede contener sublistas de puntajes.
    # Si no hay puntajes, retorna 0. Si hay puntajes, retorna el promedio con dos decimales.
    def calcular_puntaje_promedio(self,puntajes):
        if not puntajes: 
            return 0
    
        puntajes_totales = []
        for sublista in puntajes:
            if isinstance(sublista, list):
                puntajes_totales.extend(sublista)
            else:
                puntajes_totales.append(sublista)

        if not puntajes_totales:
            return 0

        promedio_general = sum(puntajes_totales) / len(puntajes_totales)
        promedio_general = "{:.2f}".format(promedio_general)
        return promedio_general

    # Esta función obtiene y retorna una lista de puntajes de reseñas de un vino en un período de tiempo específico realizadas por un sommelier en particular.
    def calcular_puntaje_de_sommelier_en_periodo(self,vino,fecha_desde,fecha_hasta,sommelier):
        puntaje_resenias=[]
        for resenia in vino.get_resenia():
            if resenia.sos_de_periodo(fecha_desde, fecha_hasta, resenia.get_fecha_resenia()):
                if resenia.sos_de_somellier(sommelier):
                    puntaje_resenias.append(resenia.get_puntaje())
        return puntaje_resenias