class Categoria:

    def __init__(self, id: int, descricao: str):
        self.__id = id
        self.__descricao = descricao

    def get_id(self):
        return self.__id

    def get_descricao(self):
        return self.__descricao

    def set_id(self, id: int):
        self.__id = id

    def set_descricao(self, descricao: str):
        self.__descricao = descricao

    def to_json(self):
        return {
            "id": self.__id,
            "descricao": self.__descricao
        }

    @staticmethod
    def from_json(dic: dict):
        return Categoria(dic["id"], dic["descricao"])

    def __str__(self):
        return f"{self.__id} - {self.__descricao}"
