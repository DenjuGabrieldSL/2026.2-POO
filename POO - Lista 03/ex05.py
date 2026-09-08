class Data:
    def __init__(self, dia, mes, ano):
        if not self.DataValida(dia, mes, ano):
            raise ValueError("Data inválida.")

        self.dia = dia
        self.mes = mes
        self.ano = ano

    def GetDia(self):
        return self.dia

    def GetMes(self):
        return self.mes

    def GetAno(self):
        return self.ano

    def SetData(self, data):
        partes = data.split("/")

        if len(partes) != 3:
            raise ValueError("Formato inválido. Use dd/mm/aaaa.")

        dia = int(partes[0])
        mes = int(partes[1])
        ano = int(partes[2])

        if not self.DataValida(dia, mes, ano):
            raise ValueError("Data inválida.")

        self.dia = dia
        self.mes = mes
        self.ano = ano

    def DataValida(self, dia, mes, ano):
        if ano <= 0:
            return False

        if mes < 1 or mes > 12:
            return False

        dias_mes = [31, 28, 31, 30, 31, 30,
                    31, 31, 30, 31, 30, 31]

        # Verifica ano bissexto
        if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
            dias_mes[1] = 29

        if dia < 1 or dia > dias_mes[mes - 1]:
            return False

        return True

    def ToString(self):
        return f"{self.dia:02d}/{self.mes:02d}/{self.ano:04d}"


# Testando a classe
d = Data(8, 9, 2026)

print("Dia:", d.GetDia())
print("Mês:", d.GetMes())
print("Ano:", d.GetAno())
print("Data:", d.ToString())

d.SetData("15/10/2026")

print("Nova data:", d.ToString())

# UML - Data
#
# ┌──────────────────────────────────────┐
# │                 Data                 │
# ├──────────────────────────────────────┤
# │ - dia : int                          │
# │ - mes : int                          │
# │ - ano : int                          │
# ├──────────────────────────────────────┤
# │ + __init__(dia, mes, ano)             │
# │ + GetDia() : int                     │
# │ + GetMes() : int                     │
# │ + GetAno() : int                     │
# │ + SetData(data : string)             │
# │ + ToString() : string                │
# └──────────────────────────────────────┘