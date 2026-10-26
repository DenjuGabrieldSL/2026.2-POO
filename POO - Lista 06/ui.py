
from cliente import Cliente
from cliente_dao import ClienteDAO


class UI:

    @staticmethod
    def Menu():
        print("\n===== SISTEMA DE CLIENTES =====")
        print("1 - Listar clientes")
        print("2 - Inserir cliente")
        print("3 - Atualizar cliente")
        print("4 - Excluir cliente")
        print("0 - Finalizar")

        return int(input("Escolha uma opção: "))

    @staticmethod
    def Cliente_Listar():
        clientes = ClienteDAO.Listar()

        if len(clientes) == 0:
            print("Nenhum cliente cadastrado.")
        else:
            print("\n===== CLIENTES CADASTRADOS =====")

            for cliente in clientes:
                print(cliente)

    @staticmethod
    def Cliente_Inserir():
        print("\n===== INSERIR CLIENTE =====")

        id = int(input("ID: "))

        if ClienteDAO.Listar_Id(id) is not None:
            print("Já existe um cliente com esse ID.")
            return

        nome = input("Nome: ")
        email = input("Email: ")
        fone = input("Telefone: ")

        cliente = Cliente(id, nome, email, fone)

        ClienteDAO.Inserir(cliente)

        print("Cliente cadastrado com sucesso!")

    @staticmethod
    def Cliente_Atualizar():
        print("\n===== ATUALIZAR CLIENTE =====")

        id = int(input("Digite o ID do cliente: "))

        cliente = ClienteDAO.Listar_Id(id)

        if cliente is None:
            print("Cliente não encontrado.")
            return

        nome = input("Novo nome: ")
        email = input("Novo email: ")
        fone = input("Novo telefone: ")

        cliente.nome = nome
        cliente.email = email
        cliente.fone = fone

        ClienteDAO.Atualizar(cliente)

        print("Cliente atualizado com sucesso!")

    @staticmethod
    def Cliente_Excluir():
        print("\n===== EXCLUIR CLIENTE =====")

        id = int(input("Digite o ID do cliente: "))

        cliente = ClienteDAO.Listar_Id(id)

        if cliente is not None:
            ClienteDAO.Excluir(cliente)
            print("Cliente excluído com sucesso!")
        else:
            print("Cliente não encontrado.")

    @staticmethod
    def Main():
        ClienteDAO.Abrir()

        while True:
            try:
                opcao = UI.Menu()

                if opcao == 1:
                    UI.Cliente_Listar()

                elif opcao == 2:
                    UI.Cliente_Inserir()

                elif opcao == 3:
                    UI.Cliente_Atualizar()

                elif opcao == 4:
                    UI.Cliente_Excluir()

                elif opcao == 0:
                    print("Sistema finalizado!")
                    break

                else:
                    print("Opção inválida.")

            except ValueError:
                print("Digite um valor válido.")


UI.Main()
