class PlayList:
    def __init__(self, id, nome, descricao):
        self.set_id(id)
        self.set_nome(nome)
        self.set_descricao(descricao)
        self.__itens = []

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_descricao(self):
        return self.__descricao

    def set_descricao(self, descricao):
        self.__descricao = descricao

    def get_itens(self):
        return self.__itens

    def adicionar_item(self, item):
        self.__itens.append(item)

    def tempo_total(self, musicas):
        total = 0

        for item in self.__itens:
            for musica in musicas:
                if musica.get_id() == item.get_id_musica():
                    total += musica.get_duracao()

        return total

    def __str__(self):
        return f"ID: {self.__id} | Nome: {self.__nome} | Descrição: {self.__descricao}"