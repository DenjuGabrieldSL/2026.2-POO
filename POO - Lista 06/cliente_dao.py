
import json
from pathlib import Path
from cliente import Cliente


class ClienteDAO:

    objetos = []
    arquivo = Path(__file__).with_name("clientes.json")

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
        cliente = cls.Listar_Id(obj.id)

        if cliente is not None:
            cliente.nome = obj.nome
            cliente.email = obj.email
            cliente.fone = obj.fone
            cls.Salvar()
            return True

        return False

    @classmethod
    def Excluir(cls, obj):
        if obj in cls.objetos:
            cls.objetos.remove(obj)
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
                    cliente = Cliente(
                        item["id"],
                        item["nome"],
                        item["email"],
                        item["fone"]
                    )

                    cls.objetos.append(cliente)

    @classmethod
    def Salvar(cls):
        dados = []

        for obj in cls.objetos:
            dados.append({
                "id": obj.id,
                "nome": obj.nome,
                "email": obj.email,
                "fone": obj.fone
            })

        with open(cls.arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)
