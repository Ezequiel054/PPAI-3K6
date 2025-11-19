from ClasesEntidad.Estado import Estado
from ClasesEntidad.State.Rechazado import Rechazado
from ClasesEntidad.CambioEstado import CambioEstado

class BloqueadoEnRevision(Estado):
    def __init__(self):
        super().__init__()
        self.nombreEstado = "BloqueadoEnRevision"


    def esBloqueadoEnRevision(self):
        return self.nombreEstado.lower() == "bloqueadoenrevision"


    def rechazar(self, fechaActual, empleado, cambiosEstado, eventoSismico):
       

        self.buscarCambioEstadoActual(fechaActual,cambiosEstado)
      
        estadoRechazado = self.crearProximoEstado()
        
        cambioEstado = self.crearCambioEstado(fechaActual, estadoRechazado, empleado, eventoSismico.id)

        eventoSismico.agregarCambioEstado(cambioEstado)
        eventoSismico.setEstadoActual(estadoRechazado)



    def buscarCambioEstadoActual(self, fechaFin,cambioEstados):
        for cambioEst in cambioEstados:
            if cambioEst.esEstadoActual():
                cambioEst.setFechaFin(fechaFin)


    def crearCambioEstado(self, fecha, estado, empleado, eventoSismico_id):
        cambioEstado = CambioEstado(fechaHoraInicio= fecha, fechaHoraFin=None,
                                    estado=estado, responsableInspeccion=empleado)
        cambioEstado.saveInDB(eventoSismico_id)
        return cambioEstado


    def crearProximoEstado(self):
        estadoRechazado = Rechazado("Evento Sismico")
        return estadoRechazado
