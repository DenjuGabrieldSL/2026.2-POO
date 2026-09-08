class Viagem:
    def __init__(self, distancia, horas, minutos):
        self.distancia = distancia
        self.horas = horas
        self.minutos = minutos

    def velocidade_media(self):
        tempo_horas = self.horas + self.minutos / 60
        return self.distancia / tempo_horas

distancia = float(input("Digite a distancia percorrida (km): "))
horas = int(input("Digite as horas: "))
minutos = int(input("Digite os minutos: "))

v = Viagem(distancia, horas, minutos)

print("Velocidade media:", v.velocidade_media(), "km/h")