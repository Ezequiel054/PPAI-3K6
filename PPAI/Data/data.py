from datetime import datetime

from ClasesEntidad.ClasificacionSismo import ClasificacionSismo
from ClasesEntidad.AlcanceSismo import AlcanceSismo
from ClasesEntidad.CambioEstado import CambioEstado
from ClasesEntidad.DetalleMuestraSismica import DetalleMuestraSismica
from ClasesEntidad.Empleado import Empleado
from ClasesEntidad.EstacionSismologica import EstacionSismologica
from ClasesEntidad.Estado import Estado
from ClasesEntidad.EventoSismico import EventoSismico
from ClasesEntidad.MuestraSismica import MuestraSismica
from ClasesEntidad.OrigenDeGeneracion import OrigenDeGeneracion
from ClasesEntidad.SerieTemporal import SerieTemporal
from ClasesEntidad.Sesion import Sesion
from ClasesEntidad.Sismografo import Sismografo
from ClasesEntidad.TipoDeDato import TipoDeDato
from ClasesEntidad.Usuario import Usuario

clasificaciones = [
    ClasificacionSismo("Superficial", 0, 60),
    ClasificacionSismo("Intermedio", 61, 300),
    ClasificacionSismo("Profundo", 301, 650),
    ]

origenes = [
    OrigenDeGeneracion("Interplaca", "Sismo entre placas tectónicas"),
    OrigenDeGeneracion("Volcánico", "Sismo por actividad volcánica"),
    OrigenDeGeneracion("Explosiones", "Sismo por explosiones humanas"),
]

alcances = [
    AlcanceSismo("Local", "Hasta 100 km del epicentro"),
    AlcanceSismo("Regional", "Entre 100 y 1000 km del epicentro"),
    AlcanceSismo("Tele-sismo", "Más de 1000 km del epicentro"),
]

estados = [
    Estado("Evento Sismico", "Pendiente en revision"),
    Estado("Evento Sismico", "Autodetectado"),
    Estado("Evento Sismico", "Bloqueado en revision"),
    Estado("Evento Sismico", "Rechazado"),
    Estado("Evento Sismico", "Derivado a experto"),
    Estado("Evento Sismico", "Confirmado")
]

tiposDeDatos = [
    TipoDeDato("Velocidad de Onda", "km/seg", 100),
    TipoDeDato("Frecuencia de Onda", "Hz", 100),
    TipoDeDato("Longitud", "Km/ciclo", 100)
]

detallesMuestra = [
    [DetalleMuestraSismica(50, tiposDeDatos[0]),
    DetalleMuestraSismica(50, tiposDeDatos[1]),
    DetalleMuestraSismica(50, tiposDeDatos[2])],

    [DetalleMuestraSismica(55, tiposDeDatos[0]),
    DetalleMuestraSismica(55, tiposDeDatos[1]),
    DetalleMuestraSismica(55, tiposDeDatos[2])]
]

muestras = [
    [MuestraSismica("2025-05-20 20:15", detallesMuestra[0]),
    MuestraSismica("2025-05-20 20:20", detallesMuestra[1])],

    [MuestraSismica("2024-10-20 16:40", detallesMuestra[0]),
    MuestraSismica("2024-10-20 16:45", detallesMuestra[1])]
]

series = [
    SerieTemporal(False, "2025-05-20 20:15", "2025-05-20 20:15",
                  "5", muestras[0]),
    SerieTemporal(False, "2025-05-20 20:15", "2025-05-20 20:15",
                  "5", muestras[1])
]

eventosSismicos = [
    EventoSismico("2025-05-20 20:15", "2025-05-20 20:20", 100,
                  100,100, 100, 6,
                  clasificaciones[0], origenes[0], alcances[0], [series[0]], estados[1], []),
    EventoSismico("2024-10-20 16:40", "2024-05-20 16:50", 65,
                  65,65, 65, 4,
                  clasificaciones[1], origenes[1], alcances[0], [series[1]], estados[1], []),
    EventoSismico("2025-01-10 06:00", "2025-01-10 06:05", 87.5,
                  10.123, 10.456, -74.321, 6,
                  clasificaciones[1], origenes[2], alcances[1], [series[0]], estados[1], []),
    EventoSismico("2025-04-15 14:30", "2025-04-15 14:35", 92.3,
                  -33.789, -34.001, -70.789, 8,
                  clasificaciones[0], origenes[2], alcances[2], [series[0]], estados[1], []),
    EventoSismico("2025-07-20 22:45", "2025-07-20 22:50", 78.9,
                  35.123, 35.876, 139.654, 4,
                  clasificaciones[1], origenes[2], alcances[1], [series[0]], estados[1], [])

]

estaciones = [
    EstacionSismologica("001", "Estacion 1", 100, 100,
                        "10", "Doc",
                        "2024-12-21"),
    EstacionSismologica("001", "Estacion 2", 100, 100,
                        "10", "Doc",
                        "2024-12-21")
]

sismografos = [
    Sismografo("2024-12-22", "001", "7156",
               estaciones[0], series[0]),
    Sismografo("2024-12-22", "002", "7157",
               estaciones[1], series[1])
]

empleados = [
    Empleado("Lucía", "González")
]

usuarios = [
    Usuario("LuciaGonz", "21Lucia", empleados[0])
]

sesion = Sesion(datetime.now(), "", usuarios[0])

