from Data.dao.baseDao import BaseDAO
from Data.models.Empleado import Empleado

class EmpleadoDAO(BaseDAO):
    def __init__(self):
        super().__init__(Empleado)

    def get_by_nombre(self, nombre):
        return self.db.query(Empleado).filter_by(nombre=nombre).all()
