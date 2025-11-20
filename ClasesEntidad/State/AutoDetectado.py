from ClasesEntidad.Estado import Estado
from ClasesEntidad.CambioEstado import CambioEstado
from ClasesEntidad.State.BloqueadoEnRevision import BloqueadoEnRevision

class AutoDetectado(Estado):
    def __init__(self):
        super().__init__()
        self.nombreEstado = "Autodetectado"


    def esAutodetectado(self):
        return self.nombreEstado.lower() == "autodetectado"


    def bloquearEnRevision(self, fecha, empleado, cambiosEstado,eventoSismico):
        
        cambioEstActual = self.buscarEstadoActual(cambiosEstado)
        cambioEstActual.setFechaFin(fecha)
        
        estadoBloqueado = self.crearProximoEstado()
        cambioEstado = self.crearCambioEstado(fecha, estadoBloqueado, empleado, eventoSismico)
        eventoSismico.agregarCambioEstado(cambioEstado)

        eventoSismico.setEstadoActual(estadoBloqueado)

    def buscarEstadoActual(self,cambioEstados):
        for cambioEst in cambioEstados:
            if cambioEst.esEstadoActual():
                return cambioEst


    def crearCambioEstado(self, fecha, estado, empleado, eventoSismico_id):
        cambioEstado = CambioEstado(fechaHoraInicio= fecha, fechaHoraFin=None,
                                    estado=estado, responsableInspeccion=empleado)
        cambioEstado.saveInDB(eventoSismico_id)
        return cambioEstado


    def crearProximoEstado(self):
        estadoBloqueado = BloqueadoEnRevision("Evento Sismico")
        return estadoBloqueado
