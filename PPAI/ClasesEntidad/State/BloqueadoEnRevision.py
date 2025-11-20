from ClasesEntidad.Estado import Estado
from ClasesEntidad.State.Rechazado import Rechazado
from ClasesEntidad.CambioEstado import CambioEstado

class BloqueadoEnRevision(Estado):
    def __init__(self, ambito):
        super().__init__(ambito)
        self.nombreEstado = "BloqueadoEnRevision"


    def esBloqueadoEnRevision(self):
        return self.nombreEstado.lower() == "bloqueadoenrevision"


    def rechazar(self, fechaActual, empleado, cambiosEstado, eventoSismico):
        cambioEstadoActual = self.buscarCambioEstadoActual(cambiosEstado)
        cambioEstadoActual.setFechaFin(fechaActual)

        estadoRechazado = self.crearProximoEstado()
        cambioEstado = self.crearCambioEstado(fechaActual, estadoRechazado, empleado, eventoSismico)

        eventoSismico.agregarCambioEstado(cambioEstado)
        eventoSismico.setEstadoActual(estadoRechazado)


    def buscarCambioEstadoActual(self, cambioEstados):
        for cambioEst in cambioEstados:
            if cambioEst.esEstadoActual():
                return cambioEst


    def crearCambioEstado(self, fecha, estado, empleado, eventoSismico):
        cambioEstado = CambioEstado(fechaHoraInicio=fecha, fechaHoraFin=None,
                                    estado=estado, responsableInspeccion=empleado)
        return cambioEstado


    def crearProximoEstado(self):
        estadoRechazado = Rechazado("Evento Sismico")
        return estadoRechazado
