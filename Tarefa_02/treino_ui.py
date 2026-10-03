from treino import Treino


class TreinoUI:

    treinos = []

    @staticmethod
    def inserir():
        id = int(input("ID: "))
        data = input("Data: ")
        distancia = float(input("Distância (km): "))
        tempo = float(input("Tempo (minutos): "))

        treino = Treino(id, data, distancia, tempo)

        TreinoUI.treinos.append(treino)

        print("Treino inserido!")

    @staticmethod
    def listar():
        if len(TreinoUI.treinos) == 0:
            print("Nenhum treino cadastrado.")
        else:
            for treino in TreinoUI.treinos:
                print(treino)

    @staticmethod
    def listar_id():
        id = int(input("Digite o ID: "))

        for treino in TreinoUI.treinos:
            if treino.get_id() == id:
                print(treino)
                return

        print("Treino não encontrado.")

    @staticmethod
    def atualizar():
        id = int(input("Digite o ID do treino: "))

        for treino in TreinoUI.treinos:
            if treino.get_id() == id:

                data = input("Nova data: ")
                distancia = float(input("Nova distância (km): "))
                tempo = float(input("Novo tempo (minutos): "))

                treino.set_data(data)
                treino.set_distancia(distancia)
                treino.set_tempo(tempo)

                print("Treino atualizado!")
                return

        print("Treino não encontrado.")

    @staticmethod
    def excluir():
        id = int(input("Digite o ID do treino: "))

        for treino in TreinoUI.treinos:
            if treino.get_id() == id:
                TreinoUI.treinos.remove(treino)
                print("Treino excluído!")
                return

        print("Treino não encontrado.")

    @staticmethod
    def mais_rapido():
        if len(TreinoUI.treinos) == 0:
            print("Nenhum treino cadastrado.")
            return

        mais_rapido = TreinoUI.treinos[0]

        for treino in TreinoUI.treinos:
            pace_atual = treino.get_tempo() / treino.get_distancia()
            pace_melhor = mais_rapido.get_tempo() / mais_rapido.get_distancia()

            if pace_atual < pace_melhor:
                mais_rapido = treino

        print("Treino mais rápido:")
        print(mais_rapido)

    @staticmethod
    def main():

        while True:

            print()
            print("===== TREINOS =====")
            print("1 - Inserir")
            print("2 - Listar")
            print("3 - Listar por ID")
            print("4 - Atualizar")
            print("5 - Excluir")
            print("6 - Mais rápido")
            print("0 - Sair")

            opcao = input("Escolha: ")

            if opcao == "1":
                TreinoUI.inserir()

            elif opcao == "2":
                TreinoUI.listar()

            elif opcao == "3":
                TreinoUI.listar_id()

            elif opcao == "4":
                TreinoUI.atualizar()

            elif opcao == "5":
                TreinoUI.excluir()

            elif opcao == "6":
                TreinoUI.mais_rapido()

            elif opcao == "0":
                print("Programa encerrado.")
                break

            else:
                print("Opção inválida.")


TreinoUI.main()