from datetime import datetime


class Venda:

    def __init__(self, id: int, data: str = None, id_cliente: int = 0, total: float = 0.0):
        self.__id = id
        self.__data = data if data else datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.__id_cliente = id_cliente
        self.__total = float(total)

    def get_id(self):
        return self.__id

    def get_data(self):
        return self.__data

    def get_id_cliente(self):
        return self.__id_cliente

    def get_total(self):
        return self.__total

    def set_id(self, id: int):
        self.__id = id

    def to_json(self):
        return {
            "id": self.__id,
            "data": self.__data,
            "id_cliente": self.__id_cliente,
            "total": round(self.__total, 2)
        }

    @staticmethod
    def from_json(dic: dict):
        return Venda(dic["id"], dic.get("data"), dic.get("id_cliente", 0), dic.get("total", 0.0))

    def __str__(self):
        return f"Venda #{self.__id} - {self.__data} (Total: R$ {self.__total:.2f})"
