from models.cliente import Cliente
from models.categoria import Categoria
from models.produto import Produto
from dao.cliente_dao import ClienteDAO
from dao.categoria_dao import CategoriaDAO
from dao.produto_dao import ProdutoDAO


class Service:

    @staticmethod
    def cliente_listar():
        return ClienteDAO.get_instancia().listar()

    @staticmethod
    def cliente_inserir(nome: str, email: str, fone: str):
        c = Cliente(0, nome, email, fone)
        ClienteDAO.get_instancia().inserir(c)

    @staticmethod
    def cliente_atualizar(id: int, nome: str, email: str, fone: str):
        c = Cliente(id, nome, email, fone)
        ClienteDAO.get_instancia().atualizar(c)

    @staticmethod
    def cliente_excluir(id: int):
        c = Cliente(id, "", "", "")
        ClienteDAO.get_instancia().excluir(c)

    @staticmethod
    def categoria_listar():
        return CategoriaDAO.get_instancia().listar()

    @staticmethod
    def categoria_inserir(descricao: str):
        cat = Categoria(0, descricao)
        CategoriaDAO.get_instancia().inserir(cat)

    @staticmethod
    def categoria_atualizar(id: int, descricao: str):
        cat = Categoria(id, descricao)
        CategoriaDAO.get_instancia().atualizar(cat)

    @staticmethod
    def categoria_excluir(id: int):
        cat = Categoria(id, "")
        CategoriaDAO.get_instancia().excluir(cat)

    @staticmethod
    def produto_listar():
        return ProdutoDAO.get_instancia().listar()

    @staticmethod
    def produto_inserir(descricao: str, preco: float, id_categoria: int):
        p = Produto(0, descricao, preco, id_categoria)
        ProdutoDAO.get_instancia().inserir(p)

    @staticmethod
    def produto_atualizar(id: int, descricao: str, preco: float, id_categoria: int):
        p = Produto(id, descricao, preco, id_categoria)
        ProdutoDAO.get_instancia().atualizar(p)

    @staticmethod
    def produto_excluir(id: int):
        p = Produto(id, "", 0.0, 0)
        ProdutoDAO.get_instancia().excluir(p)

    @staticmethod
    def produto_reajustar(percentual: float):
        dao = ProdutoDAO.get_instancia()
        fator = 1.0 + (float(percentual) / 100.0)
        for p in dao.listar():
            novo_preco = max(0.0, p.get_preco() * fator)
            p.set_preco(novo_preco)
            dao.atualizar(p)
