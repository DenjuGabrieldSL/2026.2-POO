class Viagem:
    def __init__(self, destino, distancia, combustivel):
        self.set_destino(destino)
        self.set_distancia(distancia)
        self.set_combustivel(combustivel)

    # Getters
    def get_destino(self):
        return self.__destino

    def get_distancia(self):
        return self.__distancia

    def get_combustivel(self):
        return self.__combustivel

    # Setters
    def set_destino(self, destino):
        if isinstance(destino, str) and destino.strip() != "":
            self.__destino = destino
        else:
            raise ValueError("O destino deve ser um texto não vazio.")

    def set_distancia(self, distancia):
        if distancia > 0:
            self.__distancia = distancia
        else:
            raise ValueError("A distância deve ser maior que zero.")

    def set_combustivel(self, combustivel):
        if combustivel > 0:
            self.__combustivel = combustivel
        else:
            raise ValueError("A quantidade de combustível deve ser maior que zero.")

    # Calcula o consumo médio
    def consumo(self):
        return self.__distancia / self.__combustivel


class ViagemUI:

    @staticmethod
    def menu():
        print("\n===== MENU =====")
        print("1 - Calcular")
        print("2 - Fim")

        opcao = int(input("Digite a opção: "))
        return opcao

    @staticmethod
    def calculo():
        print("\n===== DADOS DA VIAGEM =====")

        destino = input("Digite o destino: ")
        distancia = float(input("Digite a distância percorrida (km): "))
        combustivel = float(
            input("Digite a quantidade de combustível gasta (litros): ")
        )

        try:
            viagem = Viagem(destino, distancia, combustivel)

            print("\n===== DADOS ARMAZENADOS =====")
            print("Destino:", viagem.get_destino())
            print("Distância:", viagem.get_distancia(), "km")
            print("Combustível:", viagem.get_combustivel(), "litros")

            print(
                "Consumo médio:",
                round(viagem.consumo(), 2),
                "km/l"
            )

        except ValueError as erro:
            print("Erro:", erro)

    @staticmethod
    def main():
        while True:
            opcao = ViagemUI.menu()

            if opcao == 1:
                ViagemUI.calculo()

            elif opcao == 2:
                print("Programa encerrado.")
                break

            else:
                print("Opção inválida.")


ViagemUI.main()
