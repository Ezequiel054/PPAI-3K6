from datetime import datetime
from Data.data import estados as dataEstados
from Data.data import eventosSismicos as dataEventos
from Data.data import sismografos as dataSismografos
from Data.data import sesiones as dataSesion
import os


class GestorRegRevisionManual:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.eventosSismicos = dataEventos # De data
        self.estados = dataEstados # De data
        self.eventosAutodetectados = {}
        self.eventoSeleccionado = None

        self.sismografos = dataSismografos # De data
        self.sesion = dataSesion[0] # De data
        self.empleadoEnSesion = None


    # PASO 2 (6)
    def opcRegRevisionManual(self):
        # Alternativo = No hay eventos autodetectados
        self.buscarEventosSismicosAutodetectados(self.eventosSismicos) # Comentar para alternativo 1

        self.empleadoEnSesion = self.buscarEmpleadoEnSesion()

        seleccion = None
        datosEventosAutodetectados = None
        if len(self.eventosAutodetectados) > 0:
            self.eventosAutodetectados = self.ordenarEventos(self.eventosAutodetectados)
            datosEventosAutodetectados = self.obtenerDatosPrincipales(self.eventosAutodetectados)
            seleccion = self.pantalla.mostrarEventosSismicosASeleccionar(datosEventosAutodetectados)
        else:
            self.pantalla.noHayEventosParaMostrar()

        if seleccion and datosEventosAutodetectados:
            self.eventoSeleccionado = datosEventosAutodetectados[seleccion]


    def buscarEventosSismicosAutodetectados(self, eventos):
        print("Buscar Eventos Sismicos Autodetectados")
        for id, ev in eventos.items():
            if ev.esAutodetectado():
               self.eventosAutodetectados.update({id: ev})


    def buscarEmpleadoEnSesion(self):
        print("Buscar Empleado En Sesion")
        return self.sesion.getEmpleado()


    def obtenerDatosPrincipales(self, eventos):
        print("Obtener Datos Principales Eventos Sismicos")
        datosEventosAutodetectados = {}
        for id, ev in eventos.items():
            datosEventosAutodetectados[id] = ev.obtenerDatosPrincipales()

        return datosEventosAutodetectados


    def ordenarEventos(self, eventos):
        print("Ordenando Eventos")
        if eventos:
            return dict(sorted(eventos.items(), key=lambda e: e[1].fechaHoraOcurrencia))


    # PASO 4 y 5 (8 y 9)
    def tomarSeleccionEventoSismico(self, id_evento):
        self.eventoSeleccionado = [id_evento, self.eventosAutodetectados[id_evento]]
        print("Tomar Seleccion Evento Sismico", self.eventoSeleccionado)
        print(self.eventoSeleccionado[1].estadoActual.nombreEstado)
        self.bloquearEventoSeleccionado(self.eventoSeleccionado)

        print(self.eventoSeleccionado[1].estadoActual.nombreEstado)

        datosYSerieEvento = self.buscarDatosEventoSismicoSeleccionado(self.eventoSeleccionado)
        # datosYSerieEvento = [datosEvento, [ [serie1, datosSerie1], [serie2, datosSerie2] ] ]
        series = []
        for i in range(0, len(datosYSerieEvento[1])):
            series.append(datosYSerieEvento[1][i][0])
            datosYSerieEvento[1][i] = datosYSerieEvento[1][i][1]

        seriesPorEstacion = self.clasificarDatosPorEstacionSismografa(self.sismografos, series)
        sismogramasPorEst = self.generarSismografa(seriesPorEstacion)

        self.pantalla.mostrarDatosEventosSismicos(datosYSerieEvento, sismogramasPorEst)


    def bloquearEventoSeleccionado(self, evento):
        # estadoBloqueadoEnRevision = self.buscarEstadoBloqueado()
        fecha = self.getFechaHoraActual()
        print("Bloquear Evento Seleccionado:", evento)
        evento[1].bloquearEnRevision(fecha, self.empleadoEnSesion)
        print("Bloquear Evento")


    def getFechaHoraActual(self):
        print("Obtener fecha")
        return datetime.now()


    def buscarDatosEventoSismicoSeleccionado(self, evento):
        print("Buscar Otros Datos Evento")
        datosEvento = evento.getDatosRestantes()
        series = self.obtenerDatosSerieTemporal(evento)
        return [datosEvento, series]


    def obtenerDatosSerieTemporal(self, evento):
        series = evento.obtenerDatosSerieTemporal()
        return series


    def clasificarDatosPorEstacionSismografa(self, sismografos, seriesObtenidas):
        seriesPorEstacion = {}
        for serie in seriesObtenidas:
            estacionSismologica = serie.obtenerSismografo(sismografos)

            if estacionSismologica not in seriesPorEstacion:
                seriesPorEstacion[estacionSismologica] = []
            seriesPorEstacion[estacionSismologica].append(serie)
        
        # Convertir diccionario a array
        arraySeriesPorEstacion = [[estacion, series] for estacion, series in seriesPorEstacion.items()]

        return arraySeriesPorEstacion


    def generarSismografa(self, seriesPorEstacion):
        sismogramasPorEst = []
        for serieEst in seriesPorEstacion:
            sismogramasPorEst.append([serieEst[0],
                                      self.llamarCUGenerarSismograma(serieEst[1])])
        return sismogramasPorEst


    def llamarCUGenerarSismograma(self, serie):
        return os.path.join(os.path.dirname(__file__), "sismograma.jpg")


    def tomarOpcionConfirmacionMapa(self):
        self.pantalla.habilitarOpcionModificarDatosEvento()


    def tomarOpcionModificarDatosEvento(self):
        self.pantalla.mostrarOpcionesParaSeleccionar()


    # PASO 12 Y 13 (16 Y 17)
    def tomarSeleccionAccion(self):
        self.validarDatosMinimos()
        print(self.eventoSeleccionado.estadoActual.nombreEstado)
        self.rechazarEvento()
        print(self.eventoSeleccionado.estadoActual.nombreEstado)
        self.finCU()


    def validarDatosMinimos(self):
        pass

    def rechazarEvento(self):
        #estadoRechazado = self.buscarEstadoRechazado(self.estados)
        fechaHora = self.getFechaHoraActual()
        self.eventoSeleccionado.rechazarEvento(fechaHora, self.empleadoEnSesion)
        print("Rechazar Evento")


    def finCU(self):
        print("Fin del CU")


    # Alternativo = Confirmar Evento
    def confirmarEvento(self):
        estadoConfirmado = self.buscarEstadoConfirmado(self.estados)
        fechaHora = self.getFechaHoraActual()
        self.eventoSeleccionado.confirmar(estadoConfirmado, fechaHora, self.empleadoEnSesion)
        print("Confirmar Evento")

    def buscarEstadoConfirmado(self, estados):
        print("Buscar Estado Rechazado")
        for est in estados:
            if est.esConfirmado() and est.esAmbitoEventoSismico():
                return est
        return None

