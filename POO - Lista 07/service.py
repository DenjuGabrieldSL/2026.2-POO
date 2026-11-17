
from cliente import Cliente
from categoria import Categoria
from produto import Produto

from cliente_dao import ClienteDAO
from categoria_dao import CategoriaDAO
from produto_dao import ProdutoDAO


class Service:

    # CLIENTES

    @staticmethod
    def cliente_inserir(nome, email, fone):
        id = max([obj.id for obj in ClienteDAO.Listar()], default=0) + 1

        cliente = Cliente(id, nome, email, fone)
        ClienteDAO.Inserir(cliente)

    @staticmethod
    def cliente_listar():
        return ClienteDAO.Listar()

    @staticmethod
    def cliente_listar_id(id):
        return ClienteDAO.Listar_Id(id)

    @staticmethod
    def cliente_atualizar(id, nome, email, fone):
        cliente = Cliente(id, nome, email, fone)
        return ClienteDAO.Atualizar(cliente)

    @staticmethod
    def cliente_excluir(id):
        return ClienteDAO.Excluir(id)

    # CATEGORIAS

    @staticmethod
    def categoria_inserir(descricao):
        id = max([obj.id for obj in CategoriaDAO.Listar()], default=0) + 1

        categoria = Categoria(id, descricao)
        CategoriaDAO.Inserir(categoria)

    @staticmethod
    def categoria_listar():
        return CategoriaDAO.Listar()

    @staticmethod
    def categoria_listar_id(id):
        return CategoriaDAO.Listar_Id(id)

    @staticmethod
    def categoria_atualizar(id, descricao):
        categoria = Categoria(id, descricao)
        return CategoriaDAO.Atualizar(categoria)

    @staticmethod
    def categoria_excluir(id):
        return CategoriaDAO.Excluir(id)

    # PRODUTOS

    @staticmethod
    def produto_inserir(descricao, preco, estoque, idCategoria):
        id = max([obj.id for obj in ProdutoDAO.Listar()], default=0) + 1

        produto = Produto(id, descricao, preco, estoque, idCategoria)
        ProdutoDAO.Inserir(produto)

    @staticmethod
    def produto_listar():
        return ProdutoDAO.Listar()

    @staticmethod
    def produto_listar_id(id):
        return ProdutoDAO.Listar_Id(id)

    @staticmethod
    def produto_atualizar(id, descricao, preco, estoque, idCategoria):
        produto = Produto(id, descricao, preco, estoque, idCategoria)
        return ProdutoDAO.Atualizar(produto)

    @staticmethod
    def produto_excluir(id):
        return ProdutoDAO.Excluir(id)

    @staticmethod
    def produto_reajustar(percentual):
        produtos = ProdutoDAO.Listar()

        for produto in produtos:
            produto.preco = produto.preco * (1 + percentual / 100)

        ProdutoDAO.Salvar()

    # ABRIR DADOS

    @staticmethod
    def abrir():
        ClienteDAO.Abrir()
        CategoriaDAO.Abrir()
        ProdutoDAO.Abrir()
