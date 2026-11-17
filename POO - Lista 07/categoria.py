
class Categoria:

    def __init__(self, id, descricao):
        self.__id = id
        self.__descricao = descricao

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    def __str__(self):
        return f"ID: {self.__id} | Descrição: {self.__descricao}"
