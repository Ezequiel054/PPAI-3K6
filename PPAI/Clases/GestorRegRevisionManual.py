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
    def opcRegRevisionManual(self):
            self.buscarEventosSísmicosAutodetectados()
            self.buscarEmpleadoEnSesion()

    def buscarEventosSísmicosAutodetectados(self):
        eventosAutodetectados = []
        for evento in self._todosEventosSismicos:
            
            if evento.esAutodectado():
                nuevoEventoAutoDetectado = self.obtenerDatosPrincipales(evento)
                eventosAutodetectados.append(nuevoEventoAutoDetectado)
                        
        eventos_sismicos_ordenados_fecha = self.ordenarEventos(eventosAutodetectados)
        self._PantallaRegRevisionManual.mostrarEventosSismicosASeleccionar(eventos_sismicos_ordenados_fecha)

    def obtenerDatosPrincipales(self, eventoSismicoSeleccionado):
        return eventoSismicoSeleccionado.obtenerDatosPrincipales()
    

    def ordenarEventos(self,eventosAutodetectados):
        eventosOrdenados = sorted(eventosAutodetectados, key=lambda item: item["FechaHoraOcurrencia"])
        return eventosOrdenados

    ## ACA SE HACE PASO 4 Y 5
    #####
    ###
    ##
    def tomarSeleccionEventoSismico(self, eventoSismicoSeleccionado):
        
        self.eventoSismicoSeleccionado = eventoSismicoSeleccionado
        
        self.bloquearEventoSeleccionado(eventoSismicoSeleccionado)

        self.buscarDatosEventosSisimicoSeleccionado(eventoSismicoSeleccionado)
        self.clasificarDatosPorEstacionSismologica()
        sismograma = self.generarSismograma()
        
        self._PantallaRegRevisionManual.mostrarDatosEventosSismicos(self.datosAlcanceClasificacionOrigen, self.datosSeriesTemporalesPorEstacion)
        self._PantallaRegRevisionManual.mostrarSismograma(sismograma)
        self._PantallaRegRevisionManual.habilitarOpcionVisualizarMapa()
        self._PantallaRegRevisionManual.habilitarOpcionModificarDatosEvento()

        self._PantallaRegRevisionManual.mostrarOpcionesParaSeleccionar()

     

#########################


    def bloquearEventoSeleccionado(self,eventoSeleccionado):
        bloqueadoEnRevision = self.buscarEstadoBloqueado()
        fechaActual = self.getFechaHoraActual
        self.bloquearEventoSismico(eventoSeleccionado, fechaActual, bloqueadoEnRevision)



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


    def buscarDatosEventosSisimicoSeleccionado(self, eventoSeleccionado):
        self.datosAlcanceClasificacionOrigen = eventoSeleccionado.getDatosRestantes()
        self.datosSeriesTemporalesPorEstacion = self.obtenerDatosSeriesTemporal(eventoSeleccionado)



    def obtenerDatosSeriesTemporal(self,eventoSeleccionado):
        datosSeriesTemporalesPorEstacion = eventoSeleccionado.obtenerDatosSeriesTemporal()

        return datosSeriesTemporalesPorEstacion

    def clasificarDatosPorEstacionSismologica(self):
        ## aca ordenar la lista self.datosSeriesTemporalesPorEstacion por numero de estacion
        pass

    def generarSismograma(self):
        self.llamarCUGenerarSismograma()


    def llamarCUGenerarSismograma(self):
        ## aca se retorna un grafico modo imagen creo, no se implementa la llamada al cu
        pass

    def tomarOpcionConfirmacionMapa(self):
        pass

    def tomarOpcionModificarDatosEvento(self):
        pass

    def tomarSeleccionAccion(self, seleccionAccion):
        self.seleccionAccion = seleccionAccion

        self.validarDatosMinimos()
        self.buscarEstadoRechazado()
        self.getFechaHoraActual()
        self.rechazarEvento()


    def validarDatosMinimos(self):
        if self.datosAlcanceClasificacionOrigen is not None and self.seleccionAccion is not None:
            return True
        return False


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

    def finCU(self):
        pass