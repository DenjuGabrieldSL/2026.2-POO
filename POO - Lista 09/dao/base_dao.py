import json
import os


class BaseDAO:

    def __init__(self, filename: str, model_cls):
        self.__filename = filename
        self.__model_cls = model_cls
        self._objetos = []
        self.abrir()

    def _proximo_id(self) -> int:
        if not self._objetos:
            return 1
        return max(obj.get_id() for obj in self._objetos) + 1

    def inserir(self, obj):
        obj.set_id(self._proximo_id())
        self._objetos.append(obj)
        self.salvar()

    def listar(self):
        self.abrir()
        return self._objetos

    def listar_id(self, id: int):
        self.abrir()
        for obj in self._objetos:
            if obj.get_id() == id:
                return obj
        return None

    def atualizar(self, obj):
        existente = self.listar_id(obj.get_id())
        if existente is not None:
            self._objetos.remove(existente)
            self._objetos.append(obj)
            self._objetos.sort(key=lambda x: x.get_id())
            self.salvar()

    def excluir(self, obj):
        existente = self.listar_id(obj.get_id())
        if existente is not None:
            self._objetos.remove(existente)
            self.salvar()

    def abrir(self):
        self._objetos = []
        if os.path.exists(self.__filename):
            with open(self.__filename, "r", encoding="utf-8") as arquivo:
                conteudo = json.load(arquivo)
                for item in conteudo:
                    self._objetos.append(self.__model_cls.from_json(item))

    def salvar(self):
        with open(self.__filename, "w", encoding="utf-8") as arquivo:
            json.dump([obj.to_json() for obj in self._objetos], arquivo, indent=4, ensure_ascii=False)
