import math

class Retangulo:
    def __init__(self, b, h):
        if b <= 0 or h <= 0:
            raise ValueError("A base e a altura devem ser positivas.")
        self.b = b
        self.h = h

    def SetBase(self, b):
        if b <= 0:
            raise ValueError("A base deve ser positiva.")
        self.b = b

    def SetAltura(self, h):
        if h <= 0:
            raise ValueError("A altura deve ser positiva.")
        self.h = h

    def GetBase(self):
        return self.b
    def GetAltura(self):
        return self.h
    def CalcArea(self):
        return self.b * self.h
    def CalcDiagonal(self):
        return math.sqrt(self.b ** 2 + self.h ** 2)
    def ToString(self):
        return f"Base: {self.b}, Altura: {self.h}"

# Testando a classe
r = Retangulo(3, 4)

print("Base:", r.GetBase())
print("Altura:", r.GetAltura())
print("Área:", r.CalcArea())
print("Diagonal:", r.CalcDiagonal())
print(r.ToString())