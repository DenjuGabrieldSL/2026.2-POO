
import json
from pathlib import Path
from produto import Produto


class ProdutoDAO:

    objetos = []
    arquivo = Path(__file__).with_name("produtos.json")

    @classmethod
    def Inserir(cls, obj):
        cls.objetos.append(obj)
        cls.Salvar()

    @classmethod
    def Listar(cls):
        return cls.objetos

    @classmethod
    def Listar_Id(cls, id):
        for obj in cls.objetos:
            if obj.id == id:
                return obj
        return None

    @classmethod
    def Atualizar(cls, obj):
        produto = cls.Listar_Id(obj.id)

        if produto is not None:
            produto.descricao = obj.descricao
            produto.preco = obj.preco
            produto.estoque = obj.estoque
            produto.idCategoria = obj.idCategoria
            cls.Salvar()
            return True

        return False

    @classmethod
    def Excluir(cls, id):
        produto = cls.Listar_Id(id)

        if produto is not None:
            cls.objetos.remove(produto)
            cls.Salvar()
            return True

        return False

    @classmethod
    def Abrir(cls):
        if cls.arquivo.exists():
            with open(cls.arquivo, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
                cls.objetos = []

                for item in dados:
                    produto = Produto(
                        item["id"],
                        item["descricao"],
                        item["preco"],
                        item["estoque"],
                        item["idCategoria"]
                    )
                    cls.objetos.append(produto)

    @classmethod
    def Salvar(cls):
        dados = []

        for obj in cls.objetos:
            dados.append({
                "id": obj.id,
                "descricao": obj.descricao,
                "preco": obj.preco,
                "estoque": obj.estoque,
                "idCategoria": obj.idCategoria
            })

        with open(cls.arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)
