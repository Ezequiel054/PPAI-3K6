
from datetime import datetime, timedelta
import random

from Clases.Empleado import Empleado
from Clases.Estado import Estado
from Clases.Usuario import Usuario
from Clases.Sesion import Sesion
from Clases.EventoSismico import EventoSismico
from Clases.CambioEstado import CambioEstado
from Clases.AlcanceSismo import AlcanceSismo
from Clases.ClasificacionSismo import ClasificacionSismo
from Clases.OrigenDeGeneracion import OrigenDeGeneracion
from Clases.SerieTemporal import SerieTemporal
from Clases.TipoDeDato import TipoDeDato
from Clases.MuestraSismica import MuestraSismica
from Clases.DetalleMuestra import DetalleMuestra
from Clases.EstacionSismologica import EstacionSismologica
from Clases.Sismografo import Sismografo


# Generador de eventos

def generar_eventos_sismicos(n):
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

    eventos = []
    estados = generar_estados()
    
    for _ in range(n):
        fecha_ocurrencia = datetime.now().replace(microsecond=0) - timedelta(days=random.randint(0, 365))
        fecha_fin = fecha_ocurrencia + timedelta(minutes=random.randint(1, 30))

        lat_epicentro = round(random.uniform(-90, 90), 6)
        lon_epicentro = round(random.uniform(-180, 180), 6)
        lat_hipocentro = round(random.uniform(-90, 90), 6)
        lon_hipocentro = round(random.uniform(-180, 180), 6)

        magnitud = round(random.uniform(2.0, 9.5), 1)

        clasificacion = random.choice(clasificaciones)
        origen = random.choice(origenes)
        alcance = random.choice(alcances)
        
        cambios_estado = generar_cambioEstado()
        estadoactual = estados[1]
        actualCambioEstado = CambioEstado(estadoactual, datetime.now())
        cambios_estado.append(actualCambioEstado)
        serieTemporal = generar_st()
        
        ''' def __init__(self,fechaHoraFin,FechaHoraOcurrencia,latitudEpicentro,latitudHipocentro,longitudEpicentro,
                 longitudHipocentro, valorMagnitud, estadoActual,
                 cambioEstado, alcanceSismo, origenGeneracion, clasificacion,serieTemporal):
        '''
        evento = EventoSismico(
            fecha_fin,
            fecha_ocurrencia,
            lat_epicentro,
            lat_hipocentro,
            lon_epicentro,
            lon_hipocentro,
            magnitud,
            estadoactual,
            cambios_estado,
            alcance,
            origen,
            clasificacion,
            serieTemporal
            
        )
        eventos.append(evento) 
        
    return eventos

def generar_estados():
    # Crear los objetos Estado
    estado_1 = Estado("Evento Sismico", "Pendiente en revision")
    estado_2 = Estado("Evento Sismico", "Autodetectado")
    estado_3 = Estado("Evento Sismico", "Bloqueado en revision")
    estado_4 = Estado("Evento Sismico", "Rechazado")
    estado_5 = Estado("Evento Sismico", "derivado a experto")

    # Lista de estados, útil para insertarlos en la base de datos
    estados = [estado_1, estado_2, estado_3, estado_4, estado_5]
    return estados

def generar_cambioEstado():
    estado = generar_estados()
    # Fechas base
    ahora = datetime.now()

    # Crear 5 cambios de estado
    cambio_1 = CambioEstado(estado[1],ahora - timedelta(days=3), ahora - timedelta(days=2))
    cambio_2 = CambioEstado(estado[2],ahora - timedelta(days=2), ahora - timedelta(days=1))
    cambio_3 = CambioEstado(estado[0], ahora - timedelta(days=1), ahora)
    # cambio_4 = CambioEstado(estado[4], ahora)

    # Guardarlos en una lista
    cambios = [cambio_1, cambio_2, cambio_3]  
    return cambios  

def generar_serieTemporal():
    # Crear tipos de datos
    vel = TipoDeDato("Velocidad de onda", "Km/seg")
    frec = TipoDeDato("Frecuencia de onda", "Hz")
    long = TipoDeDato("Longitud de onda", "m")
    fecha_inicio = datetime(2025, 5, 22, 12, 0)
    
    
    ## 21/02/2025 19:05:41 
    #  Velocidad de onda,7,Km/seg 
    # Velocidad de onda,7,Km/seg 

 
    hora_muestra = fecha_inicio + timedelta(minutes=random.randint(1, 30))
    
    muestras = []
    m = MuestraSismica(hora_muestra, [])
    muestras.append(m)
    
    valor1=5
    
    valor2=1
    valor3=2

    detalle1 = DetalleMuestra(valor1, vel)
    detalle2= DetalleMuestra(valor2, frec)
    detalle3 = DetalleMuestra(valor3, long)

    for muestra in muestras:
        muestra.crearDetalleMuestra(detalle1)
        muestra.crearDetalleMuestra(detalle2)
        muestra.crearDetalleMuestra(detalle3)
    # Crear la serie temporal
    

    serie = SerieTemporal(muestras)
    return serie

    
def generar_st():
    s1= generar_serieTemporal()
    s2= generar_serieTemporal()
    s3= generar_serieTemporal()
    
    return [s1,s2,s3]

def generar_empleados():
    empleado_1 = Empleado("Lucía", "González")
    empleado_2 = Empleado("Carlos", "Pérez")
    empleado_3 = Empleado("María", "Rodríguez")
    empleado_4 = Empleado("Juan", "López")
    empleado_5 = Empleado("Sofía", "Martínez")
    empleado_6 = Empleado("Andrés", "Gómez")
    empleado_7 = Empleado("Valentina", "Díaz")
    empleado_8 = Empleado("Martín", "Ramírez")
    empleado_9 = Empleado("Camila", "Torres")

    # Agruparlos en una lista (útil para cargar en una base de datos, o iterar)
    empleados = [
        empleado_1, empleado_2, empleado_3,
        empleado_4, empleado_5, empleado_6,
        empleado_7, empleado_8, empleado_9
    ]    
    num_empleado = random.randint(0, 8)
    
    return empleados[num_empleado]

def generar_usuario():

    empleado = generar_empleados()
    usuario = Usuario(empleado)
    return usuario

def generar_sesion():
    user = generar_usuario()
    return Sesion(user)

def generarEstacionSismologica():
    # Crear 6 estaciones sismográficas
    est_1 = EstacionSismologica("Pampa Central")
    
    '''est_2 = EstacionSismografica("Cordillera Norte")
    est_3 = EstacionSismografica("Pampa Central")
    est_4 = EstacionSismografica("Litoral Este")
    est_5 = EstacionSismografica("Patagonia Sur")
    est_6 = EstacionSismografica("Altiplano Andino")

    # Guardarlos en una lista
    estaciones = [est_1, est_2, est_3, est_4, est_5, est_6]'''
    
    return est_1

# def generarSismografo(serieTemporal):
#     estacionSismologica = generarEstacionSismologica()
#     sismografo = Sismografo(estacionSismologica,serieTemporal)
#     return sismografo

def generar_estaciones():
    est_3 ="Pampa Central"
    est_4 = "Litoral Este"
    est_5 = "Patagonia Sur"
    est_6 = "Altiplano Andino"
    return est_3,est_4,est_5,est_6