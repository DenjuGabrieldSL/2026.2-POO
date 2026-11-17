
class Produto:

    def __init__(self, id, descricao, preco, estoque, idCategoria):
        self.__id = id
        self.__descricao = descricao
        self.__preco = preco
        self.__estoque = estoque
        self.__idCategoria = idCategoria

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

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, preco):
        self.__preco = preco

    @property
    def estoque(self):
        return self.__estoque

    @estoque.setter
    def estoque(self, estoque):
        self.__estoque = estoque

    @property
    def idCategoria(self):
        return self.__idCategoria

    @idCategoria.setter
    def idCategoria(self, idCategoria):
        self.__idCategoria = idCategoria

    def __str__(self):
        return f"ID: {self.__id} | Produto: {self.__descricao} | Preço: R$ {self.__preco:.2f} | Estoque: {self.__estoque} | Categoria: {self.__idCategoria}"
