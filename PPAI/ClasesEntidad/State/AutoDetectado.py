from ClasesEntidad.Estado import Estado
from ClasesEntidad.CambioEstado import CambioEstado
from ClasesEntidad.State.BloqueadoEnRevision import BloqueadoEnRevision

class AutoDetectado(Estado):
    def __init__(self, ambito):
        super().__init__(ambito)
        self.nombreEstado = "Autodetectado"


    def esAutodetectado(self):
        return self.nombreEstado.lower() == "autodetectado"


    def bloquearEnRevision(self, fecha, empleado, cambiosEstado,eventoSismico):
        
        self.buscarEstadoActual(fecha,cambiosEstado)
        
        estadoBloqueado = self.crearProximoEstado()
        
        cambioEstado = self.crearCambioEstado(fecha, estadoBloqueado, empleado)

        eventoSismico.agregarCambioEstado(cambioEstado)

        eventoSismico.setEstadoActual(estadoBloqueado)

    def buscarEstadoActual(self, fechaFin,cambioEstados):
        for cambioEst in cambioEstados:
            if cambioEst.esEstadoActual():
                cambioEst.setFechaHoraFin = fechaFin


    def crearCambioEstado(self, fecha, estado, empleado):
        cambioEstado = CambioEstado(fechaHoraInicio= fecha, fechaHoraFin=None,
                                    estado=estado, responsableInspeccion=empleado)
        return cambioEstado


    def crearProximoEstado(self):
        estadoBloqueado = BloqueadoEnRevision("Evento Sismico")
        return estadoBloqueado
