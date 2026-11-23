from dao.base_dao import BaseDAO
from models.cliente import Cliente


class ClienteDAO(BaseDAO):
    _instancia = None

    def __init__(self):
        super().__init__("clientes.json", Cliente)

    @classmethod
    def get_instancia(cls):
        if cls._instancia is None:
            cls._instancia = cls()
        return cls._instancia
