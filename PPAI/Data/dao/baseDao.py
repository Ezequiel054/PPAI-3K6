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
        model = self.mapper.to_model(entity, self.model_class) if self.mapper else self.model_class(**entity.__dict__)
        self.db.add(model)
        self.db.commit()
        self.db.refresh(model)
        return self.mapper.to_entity(model) if self.mapper else model

    def close(self):
        self.db.close()