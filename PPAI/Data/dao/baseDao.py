from Data.database import SessionLocal

class BaseDAO:
    def __init__(self, model_class, mapper=None):
        self.model_class = model_class
        self.mapper = mapper
        self.db = SessionLocal()

    def get_all(self):
        result = self.db.query(self.model_class).all()
        if self.mapper:
            return [self.mapper.to_entity(r) for r in result]
        return result

    def create(self, entity):
        # Si ya es una instancia del modelo SQLAlchemy, persistirla directamente
        if isinstance(entity, self.model_class) or hasattr(entity, "__table__"):
            model = entity
        else:
            if self.mapper:
                # El mapper siempre debe devolver un modelo SQLAlchemy o datos para construirlo
                model = self.mapper.to_model(entity, self.model_class) if hasattr(self.mapper, "to_model") else self.mapper(entity)
            else:
                model_data = {}

                for attr, value in entity.__dict__.items():
                    if attr.startswith("_"):
                        continue

                    # Si es un objeto con id, usar solo el id
                    if hasattr(value, "id"):
                        model_data[f"{attr}_id"] = value.id
                    else:
                        model_data[attr] = value

                model = self.model_class(**model_data)

        self.db.add(model)
        self.db.commit()
        self.db.refresh(model)
        return self.mapper.to_entity(model) if self.mapper else model

    def update_field(self, id, field_name, new_value):
        """
        Actualiza un campo específico de un registro identificado por su ID.
        """
        # Buscar el registro por ID
        instance = self.db.query(self.model_class).get(id)
        if not instance:
            return None

        # Verificar que el campo exista en el modelo
        if not hasattr(instance, field_name):
            raise AttributeError(f"'{self.model_class.__name__}' no tiene el campo '{field_name}'")

        # Asignar el nuevo valor
        setattr(instance, field_name, new_value)

        # Confirmar los cambios
        self.db.commit()
        self.db.refresh(instance)

        # Devolver el resultado en formato entidad si hay mapper
        return self.mapper.to_entity(instance) if self.mapper else instance


    def close(self):
        self.db.close()