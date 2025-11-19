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
        if self.mapper:
            # El mapper siempre debe devolver un dict solo con tipos primitivos
            model = self.mapper.to_model(entity, self.model_class)
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

        :param id: ID del registro a actualizar.
        :param field_name: Nombre del campo a modificar.
        :param new_value: Nuevo valor a asignar al campo.
        :return: La entidad actualizada (o el modelo si no hay mapper).
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