from Data.dao.baseDao import BaseDAO
from Data.models.EventoSismico import EventoSismicoModel
from Data.models.CambioEstado import CambioEstadoModel

class EventoSismicoDao(BaseDAO):

    def __init__(self, db):
        super().__init__(db, EventoSismicoModel)
        self.mapa_evento_id = {}

    def registrarEvento(self, evento_obj, id_db):
        # Se llama al cargar desde la DB
        self.mapa_evento_id[id(evento_obj)] = id_db

    def persistirCambiosEstado(self, evento_obj):
        evento_id = self.mapa_evento_id.get(id(evento_obj))
        if not evento_id:
            raise Exception("Evento no registrado en el DAO")

        cambios = evento_obj.cambiosEstado

        # 1. Update del cambioEstado anterior
        cambio_actual = cambios[-2]   # el penúltimo es el anterior
        self.db.query(CambioEstadoModel).filter_by(id=cambio_actual.id_db).update({
            "fechaHoraFin": cambio_actual.fechaHoraFin
        })

        # 2. Insert del nuevo cambioEstado
        nuevo = cambios[-1]
        nuevo_model = CambioEstadoModel(
            fechaHoraInicio=nuevo.fechaHoraInicio,
            fechaHoraFin=nuevo.fechaHoraFin,
            estado_id=nuevo.estado.id_db,
            responsable_id=nuevo.responsable.id_db,
            eventoSismico_id=evento_id
        )
        self.db.add(nuevo_model)
        self.db.flush()
        nuevo.id_db = nuevo_model.id  # opcional

        # 3. Update del estadoActual del evento
        self.db.query(EventoSismicoModel).filter_by(id=evento_id).update({
            "estadoActual_id": nuevo.estado.id_db
        })

        self.db.commit()
        
    def persistirEstadoActual(self, evento):
        evento_id = self.mapa_evento_id[id(evento)]
        nuevo_estado_id = evento.estadoActual.id_db

        self.db.query(EventoSismicoModel).filter_by(id=evento_id).update({
            "estadoActual_id": nuevo_estado_id
        })
        self.db.commit()