from ClasesEntidad.Estado import Estado
from ClasesEntidad.State.Rechazado import Rechazado
from ClasesEntidad.CambioEstado import CambioEstado

class BloqueadoEnRevision(Estado):
    def __init__(self, ambito, id=2):
        super().__init__(ambito, id)
        self.nombreEstado = "BloqueadoEnRevision"


    def esBloqueadoEnRevision(self):
        return self.nombreEstado.lower() == "bloqueadoenrevision"


    def rechazar(self, fechaActual, empleado, cambiosEstado, eventoSismico):
        cambioEstadoActual = self.buscarCambioEstadoActual(fechaActual, cambiosEstado)
        if cambioEstadoActual:
            cambioEstadoActual.setFechaFin(fechaActual)  # cierra el cambio actual (solo memoria)

        estadoRechazado = self.crearProximoEstado()
        cambioEstado = self.crearCambioEstado(fechaActual, estadoRechazado, empleado, eventoSismico)

        # agregar el cambio al evento en memoria; persistencia debe hacerse fuera del dominio
        eventoSismico.agregarCambioEstado(cambioEstado)
        eventoSismico.setEstadoActual(estadoRechazado)


    def buscarCambioEstadoActual(self, fechaFin,cambioEstados):
        for cambioEst in cambioEstados:
            if cambioEst.esEstadoActual():
                return cambioEst
                # cambioEst.setFechaFin(fechaFin)


    def crearCambioEstado(self, fecha, estado, empleado, eventoSismico):
        # Crear objeto CambioEstado en memoria; no persistir aquí.
        cambioEstado = CambioEstado(fechaHoraInicio=fecha, fechaHoraFin=None,
                                    estado=estado, responsableInspeccion=empleado)
        return cambioEstado


    def crearProximoEstado(self):
        estadoRechazado = Rechazado("Evento Sismico")
        return estadoRechazado
