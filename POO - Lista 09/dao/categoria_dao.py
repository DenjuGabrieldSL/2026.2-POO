from dao.base_dao import BaseDAO
from models.categoria import Categoria


class CategoriaDAO(BaseDAO):
    _instancia = None

    def __init__(self):
        super().__init__("categorias.json", Categoria)

    @classmethod
    def get_instancia(cls):
        if cls._instancia is None:
            cls._instancia = cls()
        return cls._instancia
