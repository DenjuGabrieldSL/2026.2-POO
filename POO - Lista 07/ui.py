
from service import Service


class UI:

    @staticmethod
    def Menu():
        print("\n========== SISTEMA DE COMÉRCIO ELETRÔNICO ==========")
        print("\n--- CLIENTES ---")
        print("1 - Inserir cliente")
        print("2 - Listar clientes")
        print("3 - Atualizar cliente")
        print("4 - Excluir cliente")

        print("\n--- CATEGORIAS ---")
        print("5 - Inserir categoria")
        print("6 - Listar categorias")
        print("7 - Atualizar categoria")
        print("8 - Excluir categoria")

        print("\n--- PRODUTOS ---")
        print("9 - Inserir produto")
        print("10 - Listar produtos")
        print("11 - Atualizar produto")
        print("12 - Excluir produto")
        print("13 - Reajustar preços")

        print("\n0 - Finalizar")

        return int(input("\nEscolha uma opção: "))

    # CLIENTES

    @staticmethod
    def Cliente_Inserir():
        print("\n===== INSERIR CLIENTE =====")

        nome = input("Nome: ")
        email = input("Email: ")
        fone = input("Telefone: ")

        Service.cliente_inserir(nome, email, fone)

        print("Cliente cadastrado com sucesso!")

    @staticmethod
    def Cliente_Listar():
        clientes = Service.cliente_listar()

        print("\n===== CLIENTES CADASTRADOS =====")

        if len(clientes) == 0:
            print("Nenhum cliente cadastrado.")
        else:
            for cliente in clientes:
                print(cliente)

    @staticmethod
    def Cliente_Atualizar():
        print("\n===== ATUALIZAR CLIENTE =====")

        id = int(input("ID do cliente: "))

        cliente = Service.cliente_listar_id(id)

        if cliente is None:
            print("Cliente não encontrado.")
            return

        nome = input("Novo nome: ")
        email = input("Novo email: ")
        fone = input("Novo telefone: ")

        Service.cliente_atualizar(id, nome, email, fone)

        print("Cliente atualizado com sucesso!")

    @staticmethod
    def Cliente_Excluir():
        print("\n===== EXCLUIR CLIENTE =====")

        id = int(input("ID do cliente: "))

        if Service.cliente_excluir(id):
            print("Cliente excluído com sucesso!")
        else:
            print("Cliente não encontrado.")

    # CATEGORIAS

    @staticmethod
    def Categoria_Inserir():
        print("\n===== INSERIR CATEGORIA =====")

        descricao = input("Descrição: ")

        Service.categoria_inserir(descricao)

        print("Categoria cadastrada com sucesso!")

    @staticmethod
    def Categoria_Listar():
        categorias = Service.categoria_listar()

        print("\n===== CATEGORIAS CADASTRADAS =====")

        if len(categorias) == 0:
            print("Nenhuma categoria cadastrada.")
        else:
            for categoria in categorias:
                print(categoria)

    @staticmethod
    def Categoria_Atualizar():
        print("\n===== ATUALIZAR CATEGORIA =====")

        id = int(input("ID da categoria: "))

        categoria = Service.categoria_listar_id(id)

        if categoria is None:
            print("Categoria não encontrada.")
            return

        descricao = input("Nova descrição: ")

        Service.categoria_atualizar(id, descricao)

        print("Categoria atualizada com sucesso!")

    @staticmethod
    def Categoria_Excluir():
        print("\n===== EXCLUIR CATEGORIA =====")

        id = int(input("ID da categoria: "))

        if Service.categoria_excluir(id):
            print("Categoria excluída com sucesso!")
        else:
            print("Categoria não encontrada.")

    # PRODUTOS

    @staticmethod
    def Produto_Inserir():
        print("\n===== INSERIR PRODUTO =====")

        UI.Categoria_Listar()

        if len(Service.categoria_listar()) == 0:
            print("Cadastre uma categoria antes de inserir produtos.")
            return

        descricao = input("\nDescrição: ")
        preco = float(input("Preço: "))
        estoque = int(input("Estoque: "))
        idCategoria = int(input("ID da categoria: "))

        categoria = Service.categoria_listar_id(idCategoria)

        if categoria is None:
            print("Categoria não encontrada.")
            return

        Service.produto_inserir(
            descricao, preco, estoque, idCategoria
        )

        print("Produto cadastrado com sucesso!")

    @staticmethod
    def Produto_Listar():
        produtos = Service.produto_listar()

        print("\n===== PRODUTOS CADASTRADOS =====")

        if len(produtos) == 0:
            print("Nenhum produto cadastrado.")
        else:
            for produto in produtos:
                print(produto)

    @staticmethod
    def Produto_Atualizar():
        print("\n===== ATUALIZAR PRODUTO =====")

        id = int(input("ID do produto: "))

        produto = Service.produto_listar_id(id)

        if produto is None:
            print("Produto não encontrado.")
            return

        descricao = input("Nova descrição: ")
        preco = float(input("Novo preço: "))
        estoque = int(input("Novo estoque: "))

        UI.Categoria_Listar()

        idCategoria = int(input("Novo ID da categoria: "))

        if Service.categoria_listar_id(idCategoria) is None:
            print("Categoria não encontrada.")
            return

        Service.produto_atualizar(
            id, descricao, preco, estoque, idCategoria
        )

        print("Produto atualizado com sucesso!")

    @staticmethod
    def Produto_Excluir():
        print("\n===== EXCLUIR PRODUTO =====")

        id = int(input("ID do produto: "))

        if Service.produto_excluir(id):
            print("Produto excluído com sucesso!")
        else:
            print("Produto não encontrado.")

    @staticmethod
    def Produto_Reajustar():
        print("\n===== REAJUSTAR PREÇOS =====")

        percentual = float(
            input("Percentual de reajuste ou promoção: ")
        )

        Service.produto_reajustar(percentual)

        print("Preços atualizados com sucesso!")

    # PROGRAMA PRINCIPAL

    @staticmethod
    def Main():
        Service.abrir()

        while True:
            try:
                opcao = UI.Menu()

                if opcao == 1:
                    UI.Cliente_Inserir()

                elif opcao == 2:
                    UI.Cliente_Listar()

                elif opcao == 3:
                    UI.Cliente_Atualizar()

                elif opcao == 4:
                    UI.Cliente_Excluir()

                elif opcao == 5:
                    UI.Categoria_Inserir()

                elif opcao == 6:
                    UI.Categoria_Listar()

                elif opcao == 7:
                    UI.Categoria_Atualizar()

                elif opcao == 8:
                    UI.Categoria_Excluir()

                elif opcao == 9:
                    UI.Produto_Inserir()

                elif opcao == 10:
                    UI.Produto_Listar()

                elif opcao == 11:
                    UI.Produto_Atualizar()

                elif opcao == 12:
                    UI.Produto_Excluir()

                elif opcao == 13:
                    UI.Produto_Reajustar()

                elif opcao == 0:
                    print("\nSistema finalizado!")
                    break

                else:
                    print("Opção inválida.")

            except ValueError:
                print("Digite um valor válido.")

            except Exception as erro:
                print(f"Erro: {erro}")


UI.Main()
