class PlayListItem:
    def __init__(self, id, id_playlist, id_musica, data_inclusao, sequencia):
        self.set_id(id)
        self.set_id_playlist(id_playlist)
        self.set_id_musica(id_musica)
        self.set_data_inclusao(data_inclusao)
        self.set_sequencia(sequencia)

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_id_playlist(self):
        return self.__id_playlist

    def set_id_playlist(self, id_playlist):
        self.__id_playlist = id_playlist

    def get_id_musica(self):
        return self.__id_musica

    def set_id_musica(self, id_musica):
        self.__id_musica = id_musica

    def get_data_inclusao(self):
        return self.__data_inclusao

    def set_data_inclusao(self, data_inclusao):
        self.__data_inclusao = data_inclusao

    def get_sequencia(self):
        return self.__sequencia

    def set_sequencia(self, sequencia):
        self.__sequencia = sequencia

    def __str__(self):
        return (
            f"ID: {self.__id} | "
            f"Playlist: {self.__id_playlist} | "
            f"Música: {self.__id_musica} | "
            f"Data: {self.__data_inclusao} | "
            f"Sequência: {self.__sequencia}"
        )