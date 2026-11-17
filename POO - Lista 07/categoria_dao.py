
import json
from pathlib import Path
from categoria import Categoria


class CategoriaDAO:

    objetos = []
    arquivo = Path(__file__).with_name("categorias.json")

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
        categoria = cls.Listar_Id(obj.id)

        if categoria is not None:
            categoria.descricao = obj.descricao
            cls.Salvar()
            return True

        return False

    @classmethod
    def Excluir(cls, id):
        categoria = cls.Listar_Id(id)

        if categoria is not None:
            cls.objetos.remove(categoria)
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
                    categoria = Categoria(
                        item["id"],
                        item["descricao"]
                    )
                    cls.objetos.append(categoria)

    @classmethod
    def Salvar(cls):
        dados = []

        for obj in cls.objetos:
            dados.append({
                "id": obj.id,
                "descricao": obj.descricao
            })

        with open(cls.arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)
