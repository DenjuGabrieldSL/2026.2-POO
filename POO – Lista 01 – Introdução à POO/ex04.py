class EntradaCinema:
    def __init__(self, dia, horario):
        self.dia = dia.lower()
        self.horario = horario

    def valor_inteira(self):
        if self.dia in ["segunda", "terca", "quinta"]:
            valor = 16.0

        elif self.dia == "quarta":
            return 8.0

        else:
            valor = 20.0

        if self.horario >= 17:
            valor *= 1.5

        return valor

    def valor_meia(self):
        if self.dia == "quarta":
            return 8.0

        return self.valor_inteira() / 2


dia = input("Digite o dia: ")
horario = int(input("Digite o horario (0-23): "))

entrada = EntradaCinema(dia, horario)

print("Valor da inteira: R$", entrada.valor_inteira())
print("Valor da meia-entrada: R$", entrada.valor_meia())