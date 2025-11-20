from datetime import datetime
from Data.data import estados as dataEstados
from Data.data import eventosSismicos as dataEventos
from Data.data import sismografos as dataSismografos
from Data.data import sesiones as dataSesion
import os

# usar mappers + DAO / SessionLocal directamente
from Data.dao.baseDao import BaseDAO
from Data.models.CambioEstado import CambioEstadoModel
from Data.models.EventoSismico import EventoSismicoModel
from Data.models.Estado import EstadoModel
from Data.models.Empleado import EmpleadoModel
from Data.database import SessionLocal
from Data.mappers.CambioDeEstadoMapper import cambio_to_model


class GestorRegRevisionManual:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.eventosSismicos = dataEventos # De data
        self.estados = dataEstados # De data
        self.eventosAutodetectados = []
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
        if eventos:
            return sorted(eventos, key=lambda e: e.fechaHoraOcurrencia)


    # PASO 4 y 5 (8 y 9)
    def tomarSeleccionEventoSismico(self, indice):
        self.eventoSeleccionado = self.eventosAutodetectados[indice]

        print(self.eventoSeleccionado.estadoActual.nombreEstado)
        self.bloquearEventoSeleccionado(self.eventoSeleccionado)

        print(self.eventoSeleccionado.estadoActual.nombreEstado)

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
        evento.bloquearEnRevision(fecha, self.empleadoEnSesion)
        # Persistir el nuevo cambio y actualizar el evento en BD
        self._persistir_nuevo_cambio_y_actualizar_evento(evento, fecha)
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
        # Persistir el nuevo cambio (rechazo) y actualizar estado del evento en BD
        self._persistir_nuevo_cambio_y_actualizar_evento(self.eventoSeleccionado, fechaHora)
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





    # --- helper: persistir el último cambio creado en memoria y actualizar estado del evento ---
    def _persistir_nuevo_cambio_y_actualizar_evento(self, evento, fecha_creacion):
        # 1) Persistir cambios cerrados (fechaHoraFin != None)
        session = SessionLocal()
        dao_change = BaseDAO(CambioEstadoModel)
        for cambio in evento.cambiosEstado:
            if getattr(cambio, "fechaHoraFin", None) is not None and not getattr(cambio, "_fin_persisted", False):
                if getattr(cambio, "_db_id", None):
                    try:
                        dao_change.update_field(cambio._db_id, 'fechaHoraFin', cambio.fechaHoraFin)
                        cambio._fin_persisted = True
                    except Exception:
                        pass
                else:
                    # buscar por fechaHoraInicio y responsable (nombre/apellido) como heurística
                    q = session.query(CambioEstadoModel).filter_by(fechaHoraInicio=cambio.fechaHoraInicio)
                    if hasattr(cambio.responsableInspeccion, "nombre") and hasattr(cambio.responsableInspeccion, "apellido"):
                        emp = session.query(EmpleadoModel).filter_by(
                            nombre=cambio.responsableInspeccion.nombre,
                            apellido=cambio.responsableInspeccion.apellido
                        ).first()
                        if emp:
                            q = q.filter_by(responsableInspeccion_id=emp.id)
                    modelo = q.first()
                    if modelo:
                        modelo.fechaHoraFin = cambio.fechaHoraFin
                        session.commit()
                        cambio._db_id = modelo.id
                        cambio._fin_persisted = True

        # 2) localizar el cambio recién creado en memoria (intenta por fechaHoraInicio)
        nuevo_cambio = None
        for c in reversed(evento.cambiosEstado):
            if getattr(c, "fechaHoraInicio", None) == fecha_creacion:
                nuevo_cambio = c
                break
        if not nuevo_cambio and evento.cambiosEstado:
            nuevo_cambio = evento.cambiosEstado[-1]

        # 3) Persistir nuevo cambio si existe (mapper -> modelo -> DAO.create)
        if nuevo_cambio:
            modelo_cambio = cambio_to_model(nuevo_cambio, evento=evento)
            created = BaseDAO(CambioEstadoModel).create(modelo_cambio)
            try:
                nuevo_cambio._db_id = created.id
            except Exception:
                nuevo_cambio._db_id = getattr(created, "id", None)

        # 4) Actualizar estadoActual del Evento en BD (buscar evento_id por fecha+magnitud)
        evento_row = session.query(EventoSismicoModel).filter_by(
            fechaHoraOcurrencia=getattr(evento, "fechaHoraOcurrencia", None),
            valorMagnitud=getattr(evento, "valorMagnitud", None)
        ).first()
        if evento_row:
            estado_row = session.query(EstadoModel).filter_by(
                nombreEstado=getattr(evento.estadoActual, "nombreEstado", None),
                ambito=getattr(evento.estadoActual, "ambito", None)
            ).first()
            if estado_row:
                BaseDAO(EventoSismicoModel).update_field(evento_row.id, 'estadoActual_id', estado_row.id)

        session.close()


