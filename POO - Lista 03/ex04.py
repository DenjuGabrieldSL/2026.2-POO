import math

class EquacaoSegundoGrau:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def SetA(self, a):
        self.a = a

    def SetB(self, b):
        self.b = b

    def SetC(self, c):
        self.c = c

    def GetA(self):
        return self.a

    def GetB(self):
        return self.b

    def GetC(self):
        return self.c

    def Delta(self):
        return self.b ** 2 - 4 * self.a * self.c

    def TemRaizesReais(self):
        return self.Delta() >= 0

    def Raiz1(self):
        if not self.TemRaizesReais():
            return None

        return (-self.b + math.sqrt(self.Delta())) / (2 * self.a)

    def Raiz2(self):
        if not self.TemRaizesReais():
            return None

        return (-self.b - math.sqrt(self.Delta())) / (2 * self.a)

    def ToString(self):
        return f"a: {self.a}, b: {self.b}, c: {self.c}"


# Testando a classe
eq = EquacaoSegundoGrau(1, -5, 6)

print("A:", eq.GetA())
print("B:", eq.GetB())
print("C:", eq.GetC())
print("Delta:", eq.Delta())
print("Tem raízes reais:", eq.TemRaizesReais())
print("Raiz 1:", eq.Raiz1())
print("Raiz 2:", eq.Raiz2())
print(eq.ToString())

# UML - EquacaoSegundoGrau
#
# ┌──────────────────────────────────────┐
# │        EquacaoSegundoGrau            │
# ├──────────────────────────────────────┤
# │ - a : float                          │
# │ - b : float                          │
# │ - c : float                          │
# ├──────────────────────────────────────┤
# │ + __init__(a, b, c)                  │
# │ + SetA(a)                            │
# │ + SetB(b)                            │
# │ + SetC(c)                            │
# │ + GetA() : float                     │
# │ + GetB() : float                     │
# │ + GetC() : float                     │
# │ + Delta() : float                    │
# │ + TemRaizesReais() : bool            │
# │ + Raiz1() : float                    │
# │ + Raiz2() : float                    │
# │ + ToString() : string                │
# └──────────────────────────────────────┘