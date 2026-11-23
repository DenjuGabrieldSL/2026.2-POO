from dao.base_dao import BaseDAO
from models.venda import Venda


class VendaDAO(BaseDAO):
    _instancia = None

    def __init__(self):
        super().__init__("vendas.json", Venda)

    @classmethod
    def get_instancia(cls):
        if cls._instancia is None:
            cls._instancia = cls()
        return cls._instancia
