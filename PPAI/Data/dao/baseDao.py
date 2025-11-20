from Data.database import SessionLocal

class BaseDAO:
    def __init__(self, model_class, mapper=None, session=None):
        self.model_class = model_class
        self.mapper = mapper
        # Si se pasa session externa, usarla y no cerrarla aquí
        if session is not None:
            self.db = session
            self._session_owner = False
        else:
            self.db = SessionLocal()
            self._session_owner = True

    def get_all(self):
        result = self.db.query(self.model_class).all()
        if self.mapper:
            return [self.mapper.to_entity(r) for r in result]
        return result

    def find_one_by_filters(self, **filters):
        return self.db.query(self.model_class).filter_by(**filters).first()

    def find_evento_by_fecha_y_magnitud(self, fecha, magnitud):
        # Específico para EventoSismicoModel
        return self.find_one_by_filters(fechaHoraOcurrencia=fecha, valorMagnitud=magnitud)

    def find_estado_by_nombre_y_ambito(self, nombre, ambito):
        # Específico para EstadoModel
        return self.find_one_by_filters(nombreEstado=nombre, ambito=ambito)

    def find_cambio_by_fecha_inicio(self, fechaInicio):
        # Específico para CambioEstadoModel
        return self.find_one_by_filters(fechaHoraInicio=fechaInicio)

    def create(self, entity):
        # Si ya es una instancia del modelo SQLAlchemy, persistirla directamente
        if isinstance(entity, self.model_class) or hasattr(entity, "__table__"):
            model = entity
        else:
            if self.mapper:
                model = self.mapper.to_model(entity, self.model_class) if hasattr(self.mapper, "to_model") else self.mapper(entity)
            else:
                model_data = {}
                for attr, value in entity.__dict__.items():
                    if attr.startswith("_"):
                        continue
                    if hasattr(value, "id"):
                        model_data[f"{attr}_id"] = value.id
                    else:
                        model_data[attr] = value
                model = self.model_class(**model_data)

        self.db.add(model)
        # Si DAO es dueño de la sesión hacemos commit; si no, hacemos flush para obtener id y deferimos commit
        if self._session_owner:
            self.db.commit()
            self.db.refresh(model)
        else:
            # flush to assign PK without committing outer transaction
            self.db.flush()
            try:
                self.db.refresh(model)
            except Exception:
                # refresh puede fallar si no es necesario; ignore
                pass
        return self.mapper.to_entity(model) if self.mapper else model

    def update_field(self, id, field_name, new_value):
        # Buscar el registro por ID
        instance = self.db.query(self.model_class).get(id)
        if not instance:
            return None

        if not hasattr(instance, field_name):
            raise AttributeError(f"'{self.model_class.__name__}' no tiene el campo '{field_name}'")

        setattr(instance, field_name, new_value)

        # Commit solo si DAO creó la sesión; si no, dejar al controlador/la transacción que haga commit
        if self._session_owner:
            self.db.commit()
            self.db.refresh(instance)
        else:
            self.db.flush()
        return self.mapper.to_entity(instance) if self.mapper else instance

    def close(self):
        if self._session_owner:
            self.db.close()

# --- Helpers de persistencia centrados en la capa DAO (usar mappers + DAOs) ---
def persistir_cambios_cerrados(evento, session=None):
	"""
	Persiste fechaHoraFin de cambios cerrados en memoria.
	Se puede pasar una session para ejecutar dentro de la misma transacción.
	"""
	# IMPORT CORREGIDO: usar el nombre de clase correcto del modelo
	from Data.models.CambioEstado import CambioEstadoModel
	dao_change = BaseDAO(CambioEstadoModel, session=session)

	all_changes = dao_change.get_all() if dao_change._session_owner else dao_change.db.query(CambioEstadoModel).all()

	for cambio in evento.cambiosEstado:
		if getattr(cambio, "fechaHoraFin", None) is not None and not getattr(cambio, "_fin_persisted", False):
			# actualizar por id si la entidad ya tiene _db_id
			if getattr(cambio, "_db_id", None):
				try:
					dao_change.update_field(cambio._db_id, 'fechaHoraFin', cambio.fechaHoraFin)
					cambio._fin_persisted = True
					continue
				except Exception:
					pass

			# heurística: buscar por fechaInicio entre modelos ya cargados (mejor que cargar toda la tabla repetidamente)
			model_found = None
			for m in all_changes:
				if getattr(m, "fechaHoraInicio", None) == cambio.fechaHoraInicio:
					resp_model = getattr(m, "responsableInspeccion", None)
					if resp_model is None:
						model_found = m
						break
					ent_resp = cambio.responsableInspeccion
					if hasattr(ent_resp, "nombre") and hasattr(ent_resp, "apellido"):
						if getattr(resp_model, "nombre", None) == ent_resp.nombre and getattr(resp_model, "apellido", None) == ent_resp.apellido:
							model_found = m
							break
					else:
						model_found = m
						break

			if model_found:
				try:
					dao_change.update_field(model_found.id, 'fechaHoraFin', cambio.fechaHoraFin)
					cambio._db_id = model_found.id
					cambio._fin_persisted = True
				except Exception:
					pass

	dao_change.close()

def crear_cambio_y_vincular(evento, nuevo_cambio, session=None):
	"""
	Convierte y persiste un nuevo CambioEstado para el evento.
	Devuelve el modelo creado o None.
	"""
	# IMPORT CORREGIDO
	from Data.models.CambioEstado import CambioEstadoModel
	from Data.mappers.CambioDeEstadoMapper import cambio_to_model as mapper_cambio

	dao_change = BaseDAO(CambioEstadoModel, session=session)
	modelo_cambio = mapper_cambio(nuevo_cambio, evento=evento)
	created = dao_change.create(modelo_cambio)
	# asignar _db_id en la entidad inmediatamente (útil para evitar futuras búsquedas heurísticas)
	try:
		nuevo_cambio._db_id = created.id
	except Exception:
		nuevo_cambio._db_id = getattr(created, "id", None)
	dao_change.close()
	return created

def actualizar_estado_evento(evento, session=None):
	"""
	Busca el EventoSismicoModel correspondiente y actualiza su estadoActual_id.
	Operaciones por DAO.get_all() pero usando DAOs con la misma sesión.
	"""
	# IMPORT CORREGIDO: nombres de clases modelo exactos
	from Data.models.EventoSismico import EventoSismicoModel
	from Data.models.Estado import EstadoModel

	dao_event = BaseDAO(EventoSismicoModel, session=session)
	eventos_models = dao_event.get_all()

	evento_model = None
	for em in eventos_models:
		if getattr(em, "fechaHoraOcurrencia", None) == getattr(evento, "fechaHoraOcurrencia", None) and getattr(em, "valorMagnitud", None) == getattr(evento, "valorMagnitud", None):
			evento_model = em
			break

	if evento_model:
		dao_estado = BaseDAO(EstadoModel, session=session)
		estados_models = dao_estado.get_all()
		estado_model = None
		for es in estados_models:
			if getattr(es, "nombreEstado", None) == getattr(evento.estadoActual, "nombreEstado", None) and getattr(es, "ambito", None) == getattr(evento.estadoActual, "ambito", None):
				estado_model = es
				break
		if estado_model:
			dao_event.update_field(evento_model.id, 'estadoActual_id', estado_model.id)
		dao_estado.close()
	dao_event.close()