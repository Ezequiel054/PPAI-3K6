from Datos.datos import *

class GestorRegRevisionManual:
# Metodos inicializacion    
    def __new__(cls):
        instancia = super().__new__(cls)
        return instancia

    def __init__(self, todosEventosSismicos, pantalla):
        self._todosEventosSismicos = carga_datos()
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


    def bloquearEventoSeleccionado(self):
        pass

    def buscarEstadoBloqueado(self):
        pass

    def getFechaHoraActual(self):
        pass

    def bloquearEventoSismico(self):
        pass

    def buscarDatosEventosSisimicoSeleccionado(self):
        pass

    def obtenerDatosSeriesTemporal(self):
        pass

        
