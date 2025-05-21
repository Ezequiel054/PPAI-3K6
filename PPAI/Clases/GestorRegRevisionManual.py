from Datos.datos import *
from datetime import datetime

class GestorRegRevisionManual:
# Metodos inicializacion    
    def __new__(cls):
        instancia = super().__new__(cls)
        return instancia

    def __init__(self, todosEventosSismicos, todosEstados, pantalla, actualSesion):
        self._todosEventosSismicos = todosEventosSismicos
        self._todosEstados = todosEstados
        self._PantallaRegRevisionManual = pantalla

        ## nuevos atributos

        self.eventoSismicoSeleccionado = None
        self.datosAlcanceClasificacionOrigen = None
        self.datosSeriesTemporalesPorEstacion = None
        self.seleccionAccion = None

        self.sesion = actualSesion
        self.aSLogueado = None
        


# Metodos del Gestor
    ## PASO 1
    def opcRegRevisionManual(self):
            eventosSismicosOrdenados = self.buscarEventosSísmicosAutodetectados()
            self.buscarEmpleadoEnSesion()

            """
            A1: No hay sismos auto detectados que aún no han sido revisados

            creo que la validacion va en pantalla, que verifique si eventosSismicosOrdenados = None entonces tire el mensaje "no hay simsos..."
            """
            self._PantallaRegRevisionManual.mostrarEventosSismicosASeleccionar(eventosSismicosOrdenados)

    ## PASO 2
    def buscarEventosSísmicosAutodetectados(self):
        eventosAutodetectados = []
        for evento in self._todosEventosSismicos:
            
            if evento.esAutodectado():
                nuevoEventoAutoDetectado = self.obtenerDatosPrincipales(evento)
                eventosAutodetectados.append(nuevoEventoAutoDetectado)
                        
        eventosSismicosOrdenados = self.ordenarEventos(eventosAutodetectados)
        return eventosSismicosOrdenados
        # self._PantallaRegRevisionManual.mostrarEventosSismicosASeleccionar(eventos_sismicos_ordenados_fecha)

    def obtenerDatosPrincipales(self, eventoSismicoSeleccionado):
        return eventoSismicoSeleccionado.obtenerDatosPrincipales()
    

    def ordenarEventos(self,eventosAutodetectados):
        eventosOrdenados = sorted(eventosAutodetectados, key=lambda item: item["FechaHoraOcurrencia"])
        return eventosOrdenados

    ## PASO 3
    def tomarSeleccionEventoSismico(self, eventoSismicoSeleccionado):
        
        ### GUARDAMOS EL EVENTO SELECCIONADO COMO ATRIBUTO
        self.eventoSismicoSeleccionado = eventoSismicoSeleccionado
        
        self.bloquearEventoSeleccionado()
        
        ## PASO 5
        self.buscarDatosEventosSisimicoSeleccionado()
        self.clasificarDatosPorEstacionSismologica()
        sismograma = self.generarSismograma()
 
        self._PantallaRegRevisionManual.mostrarDatosEventosSismicos(self.datosAlcanceClasificacionOrigen, self.datosSeriesTemporalesPorEstacion)
        self._PantallaRegRevisionManual.mostrarSismograma(sismograma)
        
        ## PASO 6
        self._PantallaRegRevisionManual.habilitarOpcionVisualizarMapa()
       


     
    ## PASO 4
    def bloquearEventoSeleccionado(self):
        bloqueadoEnRevision = self.buscarEstadoBloqueado()
        fechaActual = self.getFechaHoraActual
        self.bloquearEventoSismico(self.eventoSeleccionado, fechaActual, bloqueadoEnRevision)

    def buscarEstadoBloqueado(self):

        estadoBloqueadoEnRevision = None 
        for estado in self._todosEstados:
            if estado.esAmbitoEventoSismico() and estado.esBloqueadoEnRevision():
                estadoBloqueadoEnRevision = estado
        return estadoBloqueadoEnRevision
    
    def getFechaHoraActual(self):
        return datetime.now()

    def bloquearEventoSismico(self, eventoSeleccionado, fechaActual, bloqueadoEnRevision):
        eventoSeleccionado.bloquearEnRevision(fechaActual, bloqueadoEnRevision)

    ## PASO 5
    def buscarDatosEventosSisimicoSeleccionado(self):
        self.datosAlcanceClasificacionOrigen = self.eventoSeleccionado.getDatosRestantes()
        self.datosSeriesTemporalesPorEstacion = self.obtenerDatosSeriesTemporal()



    def obtenerDatosSeriesTemporal(self):
        datosSeriesTemporalesPorEstacion = self.eventoSeleccionado.obtenerDatosSeriesTemporal()

        return datosSeriesTemporalesPorEstacion

    def clasificarDatosPorEstacionSismologica(self):
        ## aca ordenar la lista self.datosSeriesTemporalesPorEstacion por numero de estacion
        pass

    def generarSismograma(self):
        self.llamarCUGenerarSismograma()


    def llamarCUGenerarSismograma(self):
        ## aca se retorna un grafico modo imagen creo, no se implementa la llamada al cu
        pass

    ## PASO 7
    def tomarOpcionConfirmacionMapa(self, esConfirmado):
        
        if esConfirmado:
            ## aca ponemos flujo alternativos
            pass
            
        ## PASO 8
        self._PantallaRegRevisionManual.habilitarOpcionModificarDatosEvento()

 

    ## PASO 9
    def tomarOpcionModificarDatosEvento(self, esConfirmado):
        
        """  A2. El AS modifica los datos del evento sísmico. 
            Paso 8: permite la modificación de los siguientes datos del evento sísmico: magnitud, alcance y  origen de generación
        """
        if esConfirmado:
            pass

        ## PASO 10
        self._PantallaRegRevisionManual.mostrarOpcionesParaSeleccionar()



    ## PASO 11
    def tomarSeleccionAccion(self, seleccionAccion):
        self.seleccionAccion = seleccionAccion

        self.validarDatosMinimos()
        self.buscarEstadoRechazado()
        self.getFechaHoraActual()
        self.rechazarEvento()

    ## PASO 12
    def validarDatosMinimos(self):
        if self.datosAlcanceClasificacionOrigen is not None and self.seleccionAccion is not None:
            return True
        return False

    ## PASO 13
    def buscarEstadoRechazado(self):
        estadoRechazado = None 
        for estado in self._todosEstados:
            if estado.esAmbitoEventoSismico() and estado.esRechazado():
                estadoRechazado = estado
        
        return estadoRechazado

    def buscarEmpleadoEnSesion(self):
        self.sesion.getEmpleado()

    def rechazarEvento(self):
        self.eventoSismicoSeleccionado.rechazar()

    ## FIN CU
    def finCU(self):
        pass