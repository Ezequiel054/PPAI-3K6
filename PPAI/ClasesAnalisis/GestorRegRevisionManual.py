from datetime import datetime
from Data.data import estados as dataEstados
from Data.data import eventosSismicos as dataEventos
from Data.data import sismografos as dataSismografos
from Data.data import sesion as dataSesion
import os


class GestorRegRevisionManual:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.eventosSismicos = dataEventos # De data
        self.estados = dataEstados # De data
        self.eventosAutodetectados = []
        self.eventoSeleccionado = None

        self.sismografos = dataSismografos # De data
        self.sesion = dataSesion # De data


    # PASO 2 (6)
    def opcRegRevisionManual(self):
        # Alternativo = No hay eventos autodetectados
        self.buscarEventosSismicosAutodetectados(self.eventosSismicos) # Comentar para alternativo 1

        seleccion = None
        datosEventosAutodetectados = None
        if len(self.eventosAutodetectados) > 0:
            self.ordenarEventos(self.eventosAutodetectados)
            datosEventosAutodetectados = self.obtenerDatosPrincipales(self.eventosAutodetectados)
            seleccion = self.pantalla.mostrarEventosSismicosASeleccionar(datosEventosAutodetectados)
        else:
            self.pantalla.noHayEventosParaMostrar()

        if seleccion and datosEventosAutodetectados:
            self.eventoSeleccionado = datosEventosAutodetectados[seleccion]


    def buscarEventosSismicosAutodetectados(self, eventos):
        print("Buscar Eventos Sismicos Autodetectados")
        for ev in eventos:
            if ev.esAutodetectado():
                self.eventosAutodetectados.append(ev)


    def buscarEmpleadoEnSesion(self):
        print("Buscar Empleado En Sesion")
        return self.sesion.getEmpleado()


    def obtenerDatosPrincipales(self, eventos):
        print("Obtener Datos Principales Eventos Sismicos")
        datosEventosAutodetectados = []

        for ev in eventos:
            datosEventosAutodetectados.append(ev.obtenerDatosPrincipales())

        return datosEventosAutodetectados


    def ordenarEventos(self, eventos):
        print("Ordenando Eventos")
        if not eventos:
            return sorted(eventos, key=lambda e:e.fechaHoraOcurrencia)


    # PASO 4 y 5 (8 y 9)
    def tomarSeleccionEventoSismico(self, indice):
        self.eventoSeleccionado = self.eventosAutodetectados[indice]
        self.bloquearEventoSeleccionado(self.eventoSeleccionado)
        datosYSerieEvento = self.buscarDatosEventoSismicoSeleccionado(self.eventoSeleccionado)
        seriesPorEstacion = self.clasificarDatosPorEstacionSismografa(self.sismografos)
        sismogramasPorEst = self.generarSismografa(seriesPorEstacion)

        self.pantalla.mostrarDatosEventosSismicos(datosYSerieEvento, sismogramasPorEst)


    def bloquearEventoSeleccionado(self, evento):
        estadoBloqueadoEnRevision = self.buscarEstadoBloqueado()
        fecha = self.getFechaHoraActual()
        evento.bloquearEnRevision(estadoBloqueadoEnRevision, fecha, self.buscarEmpleadoEnSesion())
        print("Bloquear Evento")


    def buscarEstadoBloqueado(self):
        print("Obtener Estado Bloqueado")
        for est in self.estados:
            if est.esAmbitoEventoSismico and est.esBloqueadoEnRevision():
                return est
        return None


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


    def clasificarDatosPorEstacionSismografa(self, sismogramas):
        seriePorEstacion = []
        for sis in sismogramas:
            estacionSismologica = sis.getEstacionSismologica()
            serie = sis.getSerieTemporal()
            seriePorEstacion.append([estacionSismologica, serie])
        return seriePorEstacion


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
        self.rechazarEvento()
        self.finCU()


    def validarDatosMinimos(self):
        pass

    def rechazarEvento(self):
        estadoRechazado = self.buscarEstadoRechazado(self.estados)
        fechaHora = self.getFechaHoraActual()
        self.eventoSeleccionado.rechazar(estadoRechazado, fechaHora, self.buscarEmpleadoEnSesion())
        print("Rechazar Evento")

    def buscarEstadoRechazado(self, estados):
        print("Buscar Estado Rechazado")
        for est in estados:
            if est.esRechazado() and est.esAmbitoEventoSismico():
                return est
        return None


    def finCU(self):
        print("Fin del CU")


    # Alternativo = Confirmar Evento
    def confirmarEvento(self):
        estadoConfirmado = self.buscarEstadoConfirmado(self.estados)
        fechaHora = self.getFechaHoraActual()
        self.eventoSeleccionado.confirmar(estadoConfirmado, fechaHora, self.buscarEmpleadoEnSesion())
        print("Confirmar Evento")

    def buscarEstadoConfirmado(self, estados):
        print("Buscar Estado Rechazado")
        for est in estados:
            if est.esConfirmado() and est.esAmbitoEventoSismico():
                return est
        return None

