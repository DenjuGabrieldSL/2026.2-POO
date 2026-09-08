class Frete:
    def __init__(self, distancia, peso):
        if distancia <= 0 or peso <= 0:
            raise ValueError("A distância e o peso devem ser positivos.")

        self.distancia = distancia
        self.peso = peso

    def SetDistancia(self, distancia):
        if distancia <= 0:
            raise ValueError("A distância deve ser positiva.")
        self.distancia = distancia

    def SetPeso(self, peso):
        if peso <= 0:
            raise ValueError("O peso deve ser positivo.")
        self.peso = peso

    def GetDistancia(self):
        return self.distancia

    def GetPeso(self):
        return self.peso

    def CalcFrete(self):
        return self.distancia * self.peso * 0.01

    def ToString(self):
        return f"Distância: {self.distancia}, Peso: {self.peso}"

# Testando a classe
f = Frete(100, 50)

print("Distância:", f.GetDistancia(), "Km")
print("Peso:", f.GetPeso(), "Kg")
print("Frete: R$", f.CalcFrete())
print(f.ToString())