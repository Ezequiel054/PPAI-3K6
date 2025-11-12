from Data.database import SessionLocal

class BaseDAO:
    def __init__(self, model_class):
        self.model_class = model_class
        self.db = SessionLocal()

    def get_all(self):
        return self.db.query(self.model_class).all()

    def get_by_id(self, id):
        return self.db.get(self.model_class, id)

    def create(self, **kwargs):
        obj = self.model_class(**kwargs)
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def update(self, id, **kwargs):
        obj = self.get_by_id(id)
        if not obj:
            return None
        for key, value in kwargs.items():
            setattr(obj, key, value)
        self.db.commit()
        return obj

    def delete(self, id):
        obj = self.get_by_id(id)
        if not obj:
            return False
        self.db.delete(obj)
        self.db.commit()
        return True
    
    def close(self):
        self.db.close()
