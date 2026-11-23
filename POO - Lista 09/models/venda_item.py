class VendaItem:

    def __init__(self, id: int, id_venda: int, id_produto: int, qtd: int, preco_unit: float):
        self.__id = id
        self.__id_venda = id_venda
        self.__id_produto = id_produto
        self.__qtd = int(qtd)
        self.__preco_unit = float(preco_unit)

    def get_id(self):
        return self.__id

    def get_id_venda(self):
        return self.__id_venda

    def get_id_produto(self):
        return self.__id_produto

    def get_qtd(self):
        return self.__qtd

    def get_preco_unit(self):
        return self.__preco_unit

    def set_id(self, id: int):
        self.__id = id

    def to_json(self):
        return {
            "id": self.__id,
            "id_venda": self.__id_venda,
            "id_produto": self.__id_produto,
            "qtd": self.__qtd,
            "preco_unit": round(self.__preco_unit, 2)
        }

    @staticmethod
    def from_json(dic: dict):
        return VendaItem(
            dic["id"],
            dic.get("id_venda", 0),
            dic.get("id_produto", 0),
            dic.get("qtd", 1),
            dic.get("preco_unit", 0.0)
        )

    def __str__(self):
        return f"Item #{self.__id} - Prod {self.__id_produto} x{self.__qtd}"
