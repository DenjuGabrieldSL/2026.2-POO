class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return 3.14159 * self.raio ** 2

    def circunferencia(self):
        return 2 * 3.14159 * self.raio


raio = float(input("Digite o raio do circulo: "))

c = Circulo(raio)

print("Area:", c.area())
print("Circunferencia:", c.circunferencia())