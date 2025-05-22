from typing import List
from Datos.datos import *
from datetime import datetime
from Clases.EventoSismico import *
from Clases.Estado import *
from Clases.Sesion import *


class GestorRegRevisionManual:
# Metodos inicializacion    
    # def __new__(cls):
    #     instancia = super().__new__(cls)
    #     return instancia

    def __init__(self, pantalla):
        
        self._todosEventosSismicos = generar_eventos_sismicos(5)
        self._todosEstados = generar_estados()      
        self._PantallaRegRevisionManual = pantalla

        ## nuevos atributos

        self.eventoSismicoSeleccionado = None
        self.datosAlcanceClasificacionOrigen = None
        self.datosSeriesTemporalesPorEstacion = None
        self.seleccionAccion = None

        self.sesion = generar_sesion()
        self._aSLogueado = None
        


# Metodos del Gestor

   
    """ 
        PASO 1
    """
    def opcRegRevisionManual(self):
            eventosSismicosOrdenados = self.buscarEventosSísmicosAutodetectados()

            ## vuelve como lista de diccionario ordenados
            self.buscarEmpleadoEnSesion()

            """
            A1: No hay sismos auto detectados que aún no han sido revisados

            creo que la validacion va en pantalla, que verifique si eventosSismicosOrdenados = None entonces tire el mensaje "no hay simsos..."
            """
            self._PantallaRegRevisionManual.mostrarEventosSismicosASeleccionar(eventosSismicosOrdenados)
   
    """ 
        PASO 2
    """
    def buscarEventosSísmicosAutodetectados(self):
        eventosAutodetectados = []
        for evento in self._todosEventosSismicos:
            print(evento)
            if evento.esAutodetectado():
                nuevoEventoAutoDetectado = self.obtenerDatosPrincipales(evento)
                ## implemetna diccionario
                eventosAutodetectados.append(nuevoEventoAutoDetectado)
                        
        eventosSismicosOrdenados = self.ordenarEventos(eventosAutodetectados)
        return eventosSismicosOrdenados
    

    def obtenerDatosPrincipales(self, evento):
        return evento.obtenerDatosPrincipales()
    

    def ordenarEventos(self, eventosAutodetectados):
        eventosOrdenados = sorted(eventosAutodetectados, key=lambda item: item["fechaHoraOcurrencia"], reverse=True)
        return eventosOrdenados
    """ 
        PASO 3
    """
    def tomarSeleccionEventoSismico(self, eventoSismicoSeleccionado):
        
        ### GUARDAMOS EL EVENTO SELECCIONADO COMO ATRIBUTO
        self.eventoSismicoSeleccionado = eventoSismicoSeleccionado
         
        aux = self.eventoSismicoSeleccionado[0]
        latitud = str(aux[1])
        
        for evento in self._todosEventosSismicos:
            if str(evento.get_latitudEpicentro()) == latitud:
                print(evento.get_latitudEpicentro())
                self.eventoSismicoSeleccionado = evento
                break   
    
        self.bloquearEventoSeleccionado()
        
        ## PASO 5
        self.buscarDatosEventosSisimicoSeleccionado()
        self.clasificarDatosPorEstacionSismologica()
        sismograma = self.generarSismograma()
 
        self._PantallaRegRevisionManual.mostrarDatosEventosSismicos(self.datosAlcanceClasificacionOrigen, self.datosSeriesTemporalesPorEstacion)
        self._PantallaRegRevisionManual.mostrarSismograma(sismograma)
        
        ## PASO 6
        self._PantallaRegRevisionManual.habilitarOpcionVisualizarMapa()
       
    
    """ 
        PASO 4 cambio estado
    """
    def bloquearEventoSeleccionado(self):
        bloqueadoEnRevision = self.buscarEstadoBloqueado()
        fechaActual = self.getFechaHoraActual()
        self.bloquearEventoSismico(fechaActual, bloqueadoEnRevision)

    def buscarEstadoBloqueado(self):

        estadoBloqueadoEnRevision = None 
        for estado in self._todosEstados:
            if estado.esAmbitoEventoSismico() and estado.esBloqueadoEnRevision():
                estadoBloqueadoEnRevision = estado
        return estadoBloqueadoEnRevision
    
    def getFechaHoraActual(self):
        return datetime.now()

    def bloquearEventoSismico(self, fechaActual, estado):
        self.eventoSismicoSeleccionado.bloquearEnRevision(fechaActual, estado,self._aSLogueado)

   
    """ 
        PASO 5
    """
    def buscarDatosEventosSisimicoSeleccionado(self):
        self.datosAlcanceClasificacionOrigen = self.eventoSismicoSeleccionado.getDatosRestantes()
        self.datosSeriesTemporalesPorEstacion = self.obtenerDatosSeriesTemporal()



    def obtenerDatosSeriesTemporal(self):
        datosSeriesTemporalesPorEstacion = self.eventoSismicoSeleccionado.obtenerDatosSeriesTemporal()

        return datosSeriesTemporalesPorEstacion

    def clasificarDatosPorEstacionSismologica(self):
        ## aca ordenar la lista self.datosSeriesTemporalesPorEstacion por numero de estacion
        pass

    def generarSismograma(self):
        self.llamarCUGenerarSismograma()


    def llamarCUGenerarSismograma(self):
        ## aca se retorna un grafico modo imagen creo, no se implementa la llamada al cu
        pass

   
    """ 
        PASO 7
    """
    def tomarOpcionConfirmacionMapa(self, esConfirmado):
        
        if esConfirmado:
            ## aca ponemos flujo alternativos
            pass
            
        ## PASO 8
        self._PantallaRegRevisionManual.habilitarOpcionModificarDatosEvento()

 


    """ 
        PASO 9
    """
    def tomarOpcionModificarDatosEvento(self, esConfirmado):
        
        """  A2. El AS modifica los datos del evento sísmico. 
            (Paso 8: permite la modificación de los siguientes datos del evento sísmico: magnitud, alcance y  origen de generación)
        """
        if esConfirmado:
            ## ver como hacer la obtencion de estos valores
            magnitud,alcance,origen = 0,0,0
            self.eventoSismicoSeleccionado.modificarDatos(magnitud,alcance,origen)

        ## PASO 10
        self._PantallaRegRevisionManual.mostrarOpcionesParaSeleccionar()



   
    """ 
        PASO 11
    """
    def tomarSeleccionAccion(self, seleccionAccion):
        self.seleccionAccion = seleccionAccion

        if not self.validarDatosMinimos():
            pass

        """ 
            A3: El AS selecciona la opción Rechazar evento
            A4: El AS selecciona la opción Solicitar revisión a experto
            A5: El AS no completa los datos mínimos
            A6: Si la opción seleccionada es Confirmar evento, se actualiza el estado del evento sísmico a confirmado,
                registrando la fecha y hora actual como fecha de confirmación. y el AS logueado como responsable
            A7: Si la opción seleccionada es Solicitar revisión a experto, se actualiza el estado del evento sísmico a derivado a experto, 
                registrando la fecha y hora actual, y el AS logueado
        """
        match seleccionAccion:
                case "1":
                    self.confirmarEventoSeleccionado()
                case "2":
                    
                    self.rechazarEventoSeleccionado()
                case "3":
                    self.derivarARevisionEventoSeleccionado()
                case _:
                    pass



    ### anadir este metodo al gestor
    def rechazarEventoSeleccionado(self):
        estadoRechazado = self.buscarEstadoRechazado()
        fechaActual = self.getFechaHoraActual()
        self.rechazarEvento(fechaActual, estadoRechazado)
   
        """ 
            PASO 12
        """
    def validarDatosMinimos(self):
        if self.datosAlcanceClasificacionOrigen is not None and self.seleccionAccion is not None:
            return True
        return False

   
    """ 
        PASO 13
    """
    def buscarEstadoRechazado(self):
        for estado in self._todosEstados:
            if estado.esAmbitoEventoSismico() and estado.esRechazado():
                 return estado
        
    def rechazarEvento(self,fechaActual, estadoRechazado):
        self.eventoSismicoSeleccionado.rechazar(fechaActual, estadoRechazado,self.aSLogueado)

    

    def buscarEmpleadoEnSesion(self):
        empleado = self.sesion.getEmpleado()
        self.setAsLogueado(empleado)
   
        """ 
            FIN CU
        """
    def finCU(self):
        pass


    """ 
        A6: Si la opción seleccionada es Confirmar evento, se actualiza el estado del evento sísmico a confirmado,
            registrando la fecha y hora actual como fecha de confirmación. y el AS logueado como responsable
        A7: Si la opción seleccionada es Solicitar revisión a experto, se actualiza el estado del evento sísmico a derivado a experto, 
            registrando la fecha y hora actual, y el AS logueado
    """

    ## confrimar evento
    def confirmarEventoSeleccionado(self):
        estadoConfirmado = self.buscarEstadoConfirmado()
        fechaActual = self.getFechaHoraActual()
        self.confirmarEvento(fechaActual, estadoConfirmado,self.aSLogueado)

    def buscarEstadoConfirmado(self):
        for estado in self._todosEstados:
            if estado.esAmbitoEventoSismico() and estado.esConfirmado():
                return estado
        
    def confirmarEvento(self):
        self.eventoSismicoSeleccionado.confirmar()


    ## derivar a solicitud evento

    def derivarARevisionEventoSeleccionado(self):
        estadoDerivadoAExperto = self.buscarEstadoDerivadoAExperto()
        fechaActual = self.getFechaHoraActual()
        self.derivarARevisionEvento(fechaActual, estadoDerivadoAExperto,self.aSLogueado)

    def buscarEstadoDerivadoAExperto(self):
        for estado in self._todosEstados:
            if estado.esAmbitoEventoSismico() and estado.esDerivadoAExperto():
                return estado
        
    def derivarARevisionEvento(self,fechaActual,estadoDerivadoAExperto):
        self.eventoSismicoSeleccionado.derivarARevision(fechaActual, estadoDerivadoAExperto,self.aSLogueado)

    def setAsLogueado(self, aSLogueado):
        self._aSLogueado = aSLogueado