class EstacionSismologica:
    def __init__(self, codigoEstacion, nombre, latitud, longitud,
                 nroCertificacionAdquisicion, documentoCertificacionAdq,
                 fechaSolcitudCertificacion):
        self.codigoEstacion = codigoEstacion
        self.nombre = nombre
        self.latitud = latitud
        self.longitud = longitud
        self.nroCertificacionAdquisicion = nroCertificacionAdquisicion
        self.documentoCertificacionAdq = documentoCertificacionAdq
        self.fechaSolcitudCertificacion = fechaSolcitudCertificacion


    def getNombre(self):
        return self.nombre
