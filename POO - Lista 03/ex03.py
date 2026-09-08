class Conversor:
    def __init__(self, num):
        if num <= 0:
            raise ValueError("O número deve ser positivo.")

        self.num = num

    def SetNum(self, num):
        if num <= 0:
            raise ValueError("O número deve ser positivo.")

        self.num = num

    def GetNum(self):
        return self.num

    def Binario(self):
        return bin(self.num)[2:]

    def ToString(self):
        return f"Decimal: {self.num}, Binário: {self.Binario()}"


# Testando a classe
c = Conversor(10)

print("Decimal:", c.GetNum())
print("Binário:", c.Binario())
print(c.ToString())