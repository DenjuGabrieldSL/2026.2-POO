class Cliente:

    def __init__(self, id: int, nome: str, email: str, fone: str):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__fone = fone

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_email(self):
        return self.__email

    def get_fone(self):
        return self.__fone

    def set_id(self, id: int):
        self.__id = id

    def set_nome(self, nome: str):
        self.__nome = nome

    def set_email(self, email: str):
        self.__email = email

    def set_fone(self, fone: str):
        self.__fone = fone

    def to_json(self):
        return {
            "id": self.__id,
            "nome": self.__nome,
            "email": self.__email,
            "fone": self.__fone
        }

    @staticmethod
    def from_json(dic: dict):
        return Cliente(dic["id"], dic["nome"], dic["email"], dic["fone"])

    def __str__(self):
        return f"{self.__id} - {self.__nome} ({self.__email})"
