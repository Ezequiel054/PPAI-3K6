from datetime import datetime

from ClasesEntidad.ClasificacionSismo import ClasificacionSismo
from ClasesEntidad.AlcanceSismo import AlcanceSismo
from ClasesEntidad.DetalleMuestraSismica import DetalleMuestraSismica
from ClasesEntidad.Empleado import Empleado
from ClasesEntidad.EstacionSismologica import EstacionSismologica
from ClasesEntidad.State.AutoDetectado import AutoDetectado
from ClasesEntidad.EventoSismico import EventoSismico
from ClasesEntidad.MuestraSismica import MuestraSismica
from ClasesEntidad.OrigenDeGeneracion import OrigenDeGeneracion
from ClasesEntidad.SerieTemporal import SerieTemporal
from ClasesEntidad.Sesion import Sesion
from ClasesEntidad.Sismografo import Sismografo
from ClasesEntidad.TipoDeDato import TipoDeDato
from ClasesEntidad.Usuario import Usuario

# from Data.dao.baseDao import BaseDAO
# from Data.models.ClasificacionSismo import ClasificacionSismoModel
# from Data.mappers.ClasificacionSismoMapper import model_to_clasificacion

# dao = BaseDAO(ClasificacionSismoModel)
# clasificacionesDAO = dao.get_all()
# clasificaciones = []

# for c in clasificacionesDAO:
#     clas = model_to_clasificacion(c)
#     clasificaciones.append(clas)
#     print(clas)

# dao.close()

from datetime import datetime

# --- DAO base y modelos ---
from Data.dao.baseDao import BaseDAO
from Data.models.ClasificacionSismo import ClasificacionSismoModel
from Data.models.OrigenDeGeneracion import OrigenDeGeneracionModel
from Data.models.AlcanceSismo import AlcanceSismoModel
from Data.models.Estado import EstadoModel
from Data.models.TipoDeDato import TipoDeDatoModel
from Data.models.DetalleMuestraSismica import DetalleMuestraSismicaModel
from Data.models.MuestraSismica import MuestraSismicaModel
from Data.models.SerieTemporal import SerieTemporalModel
from Data.models.EventoSismico import EventoSismicoModel
from Data.models.EstacionSismologica import EstacionSismologicaModel
from Data.models.Sismografo import SismografoModel
from Data.models.Empleado import EmpleadoModel
from Data.models.Usuario import UsuarioModel
from Data.models.Sesion import SesionModel

# --- Mappers ---
from Data.mappers.ClasificacionSismoMapper import model_to_clasificacion
from Data.mappers.OrigenDeGeneracionMapper import model_to_origen
from Data.mappers.AlcanceSismoMapper import model_to_alcance
from Data.mappers.EstadoMapper import model_to_estado
from Data.mappers.TipoDeDatoMapper import model_to_tipo
from Data.mappers.DetalleMuestraSismicaMapper import model_to_detalle
from Data.mappers.MuestraSismicaMapper import model_to_muestra
from Data.mappers.SerieTemporalMapper import model_to_serie
from Data.mappers.EventoSismicoMapper import model_to_evento
from Data.mappers.EstacionSismologicaMapper import model_to_estacion
from Data.mappers.SismografoMapper import model_to_sismografo
from Data.mappers.EmpleadoMapper import model_to_empleado
from Data.mappers.UsuarioMapper import model_to_usuario
from Data.mappers.SesionMapper import model_to_sesion


# --- Función genérica para cargar entidades desde BD ---
def cargar_entidades(model_class, mapper_func):
    dao = BaseDAO(model_class)
    modelos = dao.get_all()
    entidades = [mapper_func(m) for m in modelos]
    if model_class == EventoSismicoModel:
        for e in modelos:
            print("Evento cargado:", e)
    dao.close()
    
    return entidades


# --- Cargar todas las entidades desde la base ---
clasificaciones = cargar_entidades(ClasificacionSismoModel, model_to_clasificacion)
origenes = cargar_entidades(OrigenDeGeneracionModel, model_to_origen)
alcances = cargar_entidades(AlcanceSismoModel, model_to_alcance)
estados = cargar_entidades(EstadoModel, model_to_estado)
tiposDeDatos = cargar_entidades(TipoDeDatoModel, model_to_tipo)
detallesMuestra = cargar_entidades(DetalleMuestraSismicaModel, model_to_detalle)
muestras = cargar_entidades(MuestraSismicaModel, model_to_muestra)
series = cargar_entidades(SerieTemporalModel, model_to_serie)


eventosSismicos = cargar_entidades(EventoSismicoModel, model_to_evento)
estaciones = cargar_entidades(EstacionSismologicaModel, model_to_estacion)
sismografos = cargar_entidades(SismografoModel, model_to_sismografo)
empleados = cargar_entidades(EmpleadoModel, model_to_empleado)
usuarios = cargar_entidades(UsuarioModel, model_to_usuario)
sesiones = cargar_entidades(SesionModel, model_to_sesion)
diccionario = {}
for d in eventosSismicos:
    diccionario.update(d)
eventosSismicos = diccionario

# --- Ejemplo de uso ---
# print("\n📊 Clasificaciones cargadas:")
# for c in clasificaciones:
#     print(" -", c)

# print("\n🌋 Orígenes cargados:")
# for o in origenes:
#     print(" -", o)

# print("\n📈 Eventos sismicos:")
# for e in eventosSismicos:
#     print(" -", e)

# print("\n✅ Carga completa de entidades desde la base de datos.")
for e in eventosSismicos:
    print("Llega al gestor el id de los eventos ",e)
