class Musica:
    def __init__(self, id, titulo, artista, album, duracao):
        self.set_id(id)
        self.set_titulo(titulo)
        self.set_artista(artista)
        self.set_album(album)
        self.set_duracao(duracao)

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def get_artista(self):
        return self.__artista

    def set_artista(self, artista):
        self.__artista = artista

    def get_album(self):
        return self.__album

    def set_album(self, album):
        self.__album = album

    def get_duracao(self):
        return self.__duracao

    def set_duracao(self, duracao):
        self.__duracao = duracao

    def __str__(self):
        return f"ID: {self.__id} | Título: {self.__titulo} | Artista: {self.__artista} | Álbum: {self.__album} | Duração: {self.__duracao} min"