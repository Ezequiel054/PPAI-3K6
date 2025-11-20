from ClasesEntidad.Estado import Estado
from ClasesEntidad.CambioEstado import CambioEstado
from ClasesEntidad.State.BloqueadoEnRevision import BloqueadoEnRevision

class AutoDetectado(Estado):
    def __init__(self, ambito, id=1):
        super().__init__(ambito, id)
        self.nombreEstado = "Autodetectado"


    def esAutodetectado(self):
        return self.nombreEstado.lower() == "autodetectado"


    def bloquearEnRevision(self, fecha, empleado, cambiosEstado,eventoSismico):
        
        self.buscarEstadoActual(fecha,cambiosEstado)
        
        estadoBloqueado = self.crearProximoEstado()
        
        cambioEstado = self.crearCambioEstado(fecha, estadoBloqueado, empleado, eventoSismico)

        # agregar el cambio al evento en memoria; persistencia fuera del dominio
        eventoSismico.agregarCambioEstado(cambioEstado)
        eventoSismico.setEstadoActual(estadoBloqueado)

    def buscarEstadoActual(self, fechaFin,cambioEstados):
        for cambioEst in cambioEstados:
            if cambioEst.esEstadoActual():
                cambioEst.setFechaFin(fechaFin)


    def crearCambioEstado(self, fecha, estado, empleado, eventoSismico):
        cambioEstado = CambioEstado(fechaHoraInicio= fecha, fechaHoraFin=None,
                                    estado=estado, responsableInspeccion=empleado)
        return cambioEstado


    def crearProximoEstado(self):
        estadoBloqueado = BloqueadoEnRevision("Evento Sismico")
        return estadoBloqueado
