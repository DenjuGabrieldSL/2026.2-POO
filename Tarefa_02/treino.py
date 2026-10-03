from datetime import date


class Treino:
    def __init__(self, id, data, distancia, tempo):
        self.set_id(id)
        self.set_data(data)
        self.set_distancia(distancia)
        self.set_tempo(tempo)

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_distancia(self):
        return self.__distancia

    def set_distancia(self, distancia):
        self.__distancia = distancia

    def get_tempo(self):
        return self.__tempo

    def set_tempo(self, tempo):
        self.__tempo = tempo

    def pace(self):
        minutos = self.__tempo / self.__distancia
        minutos_inteiros = int(minutos)
        segundos = int((minutos - minutos_inteiros) * 60)

        return f"{minutos_inteiros}:{segundos:02d} min/km"

    def __str__(self):
        return f"ID: {self.__id} | Data: {self.__data} | Distância: {self.__distancia} km | Tempo: {self.__tempo} min | Pace: {self.pace()}"