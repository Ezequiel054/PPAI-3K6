from ClasesEntidad.Estado import Estado
from ClasesEntidad.State.Rechazado import Rechazado

class BloqueadoEnRevision(Estado):
    def __init__(self, ambito, id=2):
        super().__init__(ambito, id)
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
                cambioEst.setFechaFin(fechaFin)


    def crearCambioEstado(self, fecha, estado, empleado):
        from ClasesEntidad.CambioEstado import CambioEstado
        cambioEstado = CambioEstado(fechaHoraInicio= fecha, fechaHoraFin=None,
                                    estado=estado, responsableInspeccion=empleado)
        cambioEstado.saveInDB()
        return cambioEstado


    def crearProximoEstado(self):
        estadoRechazado = Rechazado("Evento Sismico")
        return estadoRechazado
