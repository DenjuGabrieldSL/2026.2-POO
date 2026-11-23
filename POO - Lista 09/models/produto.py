class Produto:

    def __init__(self, id: int, descricao: str, preco: float, id_categoria: int):
        self.__id = id
        self.__descricao = descricao
        self.__preco = float(preco)
        self.__id_categoria = id_categoria

    def get_id(self):
        return self.__id

    def get_descricao(self):
        return self.__descricao

    def get_preco(self):
        return self.__preco

    def get_id_categoria(self):
        return self.__id_categoria

    def set_id(self, id: int):
        self.__id = id

    def set_descricao(self, descricao: str):
        self.__descricao = descricao

    def set_preco(self, preco: float):
        self.__preco = float(preco)

    def set_id_categoria(self, id_categoria: int):
        self.__id_categoria = id_categoria

    def to_json(self):
        return {
            "id": self.__id,
            "descricao": self.__descricao,
            "preco": round(self.__preco, 2),
            "id_categoria": self.__id_categoria
        }

    @staticmethod
    def from_json(dic: dict):
        return Produto(
            dic["id"],
            dic["descricao"],
            dic["preco"],
            dic.get("id_categoria", 0)
        )

    def __str__(self):
        return f"{self.__id} - {self.__descricao} (R$ {self.__preco:.2f})"
