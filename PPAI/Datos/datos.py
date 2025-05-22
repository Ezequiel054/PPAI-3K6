
from datetime import datetime, timedelta
import random

from PPAI.Clases import Empleado, Estado

# Entidades asociadas

class ClasificacionSismo:
    def __init__(self, nombre, kmProfundidadDesde, kmProfundidadHasta):
        self.nombre = nombre
        self.kmProfundidadDesde = kmProfundidadDesde
        self.kmProfundidadHasta = kmProfundidadHasta

    def getNombre(self):
        return self.nombre


class OrigenDeGeneracion:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

    def getNombre(self):
        return self.nombre


class AlcanceSismo:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

    def getNombre(self):
        return self.nombre


# Clase principal

class EventoSismico:
    def __init__(self, fechaHoraOcurrencia, fechaHoraFin,
                 latitudEpicentro, longitudEpicentro,
                 latitudHipocentro, longitudHipocentro,
                 valorMagnitud, clasificacion,
                 origenGeneracion, alcanceSismo):
        self.fechaHoraOcurrencia = fechaHoraOcurrencia
        self.fechaHoraFin = fechaHoraFin
        self.latitudEpicentro = latitudEpicentro
        self.longitudEpicentro = longitudEpicentro
        self.latitudHipocentro = latitudHipocentro
        self.longitudHipocentro = longitudHipocentro
        self.valorMagnitud = valorMagnitud
        self.clasificacion = clasificacion
        self.origenGeneracion = origenGeneracion
        self.alcanceSismo = alcanceSismo


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

        evento = EventoSismico(
            fecha_ocurrencia,
            fecha_fin,
            lat_epicentro,
            lon_epicentro,
            lat_hipocentro,
            lon_hipocentro,
            magnitud,
            clasificacion,
            origen,
            alcance
        )
        eventos.append(evento) 
    return eventos

def generar_estados():
    # Crear los objetos Estado
    estado_1 = Estado("Evento Sismico", "Pendiente en revision")
    estado_2 = Estado("Evento Sismico", "Autodetectado")
    estado_3 = Estado("Evento Sismico", "Bloqueado en revision")
    estado_4 = Estado("Evento Sismico", "Rechazado")

    # Lista de estados, útil para insertarlos en la base de datos
    estados = [estado_3, estado_2, estado_1, estado_4]
    return estados

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
    return empleados

