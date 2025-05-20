from Datos.datos import *
from datetime import datetime

class GestorRegRevisionManual:
# Metodos inicializacion    
    def __new__(cls):
        instancia = super().__new__(cls)
        return instancia

    def __init__(self, todosEventosSismicos, todosEstados, pantalla):
        self._todosEventosSismicos = todosEventosSismicos
        self._todosEstados = todosEstados
        self._PantallaRegRevisionManual = pantalla
        


# Metodos del Gestor
    def opcRegRevisionManual(self):
            self.buscarEventosSísmicosAutodetectados()

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


    def tomarSeleccionEventoSismico(self, eventoSismicoSeleccionado):
        self.bloquearEventoSeleccionado(eventoSismicoSeleccionado)

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
        self.buscarDatosEventosSisimicoSeleccionado(eventoSeleccionado)

    def buscarDatosEventosSisimicoSeleccionado(self, eventoSeleccionado):
        alcanceClasificacionOrign = eventoSeleccionado.getDatosRestantes()
        #seriesTemporales

    def obtenerDatosSeriesTemporal(self):
        ## esta mal creo
        pass

        
