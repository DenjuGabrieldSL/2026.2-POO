from dao.base_dao import BaseDAO
from models.venda_item import VendaItem


class VendaItemDAO(BaseDAO):
    _instancia = None

    def __init__(self):
        super().__init__("venda_itens.json", VendaItem)

    @classmethod
    def get_instancia(cls):
        if cls._instancia is None:
            cls._instancia = cls()
        return cls._instancia
