import json
import os
from Categoria import Categoria


class CategoriaDAO:
    def __init__(self):
        self.categorias = []

    def Inserir(self, categoria):
        if self.Listar_Id(categoria.get_id()) is not None:
            print("ID já cadastrado.")
            return False
        self.categorias.append(categoria)
        self.Salvar()
        return True

    def Listar(self):
        return self.categorias

    def Listar_Id(self, id):
        for categoria in self.categorias:
            if categoria.get_id() == id:
                return categoria
        return None

    def Atualizar(self, id, descricao):
        categoria = self.Listar_Id(id)
        if categoria is None:
            return False
        categoria.set_descricao(descricao)
        self.Salvar()
        return True

    def Excluir(self, id):
        categoria = self.Listar_Id(id)
        if categoria is None:
            return False
        self.categorias.remove(categoria)
        self.Salvar()
        return True

    def Abrir(self):
        if not os.path.exists("categorias.json"):
            return
        try:
            with open("categorias.json", "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
            self.categorias = [Categoria(d["id"], d["descricao"]) for d in dados]
        except (json.JSONDecodeError, KeyError, TypeError):
            print("Erro ao abrir categorias.json.")

    def Salvar(self):
        dados = [{"id": c.get_id(), "descricao": c.get_descricao()}
                 for c in self.categorias]
        with open("categorias.json", "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)
