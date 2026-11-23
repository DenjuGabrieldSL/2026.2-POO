from dao.base_dao import BaseDAO
from models.produto import Produto


class ProdutoDAO(BaseDAO):
    _instancia = None

    def __init__(self):
        super().__init__("produtos.json", Produto)

    @classmethod
    def get_instancia(cls):
        if cls._instancia is None:
            cls._instancia = cls()
        return cls._instancia
