from ClasesEntidad.Estado import Estado
from ClasesEntidad.CambioEstado import CambioEstado
from ClasesEntidad.State.Rechazado import Rechazado

class BloqueadoEnRevision(Estado):
    def __init__(self, ambito):
        super().__init__(ambito)
        self.nombreEstado = "BloqueadoEnRevision"


    def esBloqueadoEnRevision(self):
        return self.nombreEstado.lower() == "bloqueadoenrevision"


    def rechazar(self, fechaActual, empleado, cambiosEstado, eventoSismico):
       

        self.buscarCambioEstadoActual(fechaActual,cambiosEstado)
      
        estadoRechazado = self.crearProximoEstado()
        
        cambioEstado = self.crearCambioEstado(fechaActual, estadoRechazado, empleado)

        eventoSismico.agregarCambioEstado(cambioEstado)
        eventoSismico.setEstadoActual(estadoRechazado)



    def buscarCambioEstadoActual(self, fechaFin,cambioEstados):
        for cambioEst in cambioEstados:
            if cambioEst.esEstadoActual():
                cambioEst.setFechaHoraFin = fechaFin


    def crearCambioEstado(self, fecha, estado, empleado):
        cambioEstado = CambioEstado(fechaHoraInicio= fecha, fechaHoraFin=None,
                                    estado=estado, responsableInspeccion=empleado)
        return cambioEstado


    def crearProximoEstado(self):
        estadoRechazado = Rechazado("Evento Sismico")
        return estadoRechazado
