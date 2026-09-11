class Pais:
    def __init__(self, nome, populacao, area):
        self.set_nome(nome)
        self.set_populacao(populacao)
        self.set_area(area)

    # Getters
    def get_nome(self):
        return self.__nome

    def get_populacao(self):
        return self.__populacao

    def get_area(self):
        return self.__area

    # Setters
    def set_nome(self, nome):
        if isinstance(nome, str) and nome.strip() != "":
            self.__nome = nome
        else:
            raise ValueError("O nome do país deve ser um texto não vazio.")

    def set_populacao(self, populacao):
        if populacao > 0:
            self.__populacao = populacao
        else:
            raise ValueError("A população deve ser maior que zero.")

    def set_area(self, area):
        if area > 0:
            self.__area = area
        else:
            raise ValueError("A área deve ser maior que zero.")

    # Método para calcular a densidade
    def densidade(self):
        return self.__populacao / self.__area


class PaisUI:

    @staticmethod
    def menu():
        print("\n===== MENU =====")
        print("1 - Calcular")
        print("2 - Fim")

        opcao = int(input("Digite a opção: "))
        return opcao

    @staticmethod
    def calculo():
        print("\n===== DADOS DO PAÍS =====")

        nome = input("Digite o nome do país: ")

        populacao = int(
            input("Digite a população (habitantes): ")
        )

        area = float(
            input("Digite a área (km²): ")
        )

        try:
            pais = Pais(nome, populacao, area)

            print("\n===== DADOS ARMAZENADOS =====")
            print("Nome:", pais.get_nome())
            print("População:", pais.get_populacao(), "habitantes")
            print("Área:", pais.get_area(), "km²")

            print(
                "Densidade demográfica:",
                round(pais.densidade(), 2),
                "habitantes/km²"
            )

        except ValueError as erro:
            print("Erro:", erro)

    @staticmethod
    def main():
        while True:
            opcao = PaisUI.menu()

            if opcao == 1:
                PaisUI.calculo()

            elif opcao == 2:
                print("Programa encerrado.")
                break

            else:
                print("Opção inválida.")


PaisUI.main()
