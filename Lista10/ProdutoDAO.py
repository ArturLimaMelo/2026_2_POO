import json
import os
from Produto import Produto


class ProdutoDAO:
    def __init__(self):
        self.produtos = []

    def Inserir(self, produto):
        if self.Listar_Id(produto.get_id()) is not None:
            print("ID já cadastrado.")
            return False
        self.produtos.append(produto)
        self.Salvar()
        return True

    def Listar(self):
        return self.produtos

    def Listar_Id(self, id):
        for produto in self.produtos:
            if produto.get_id() == id:
                return produto
        return None

    def Atualizar(self, id, descricao, preco, estoque, idCategoria):
        produto = self.Listar_Id(id)
        if produto is None:
            return False
        produto.set_descricao(descricao)
        produto.set_preco(preco)
        produto.set_estoque(estoque)
        produto.set_idCategoria(idCategoria)
        self.Salvar()
        return True

    def Excluir(self, id):
        produto = self.Listar_Id(id)
        if produto is None:
            return False
        self.produtos.remove(produto)
        self.Salvar()
        return True

    def Abrir(self):
        if not os.path.exists("produtos.json"):
            return
        try:
            with open("produtos.json", "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
            self.produtos = [
                Produto(d["id"], d["descricao"], d["preco"],
                        d["estoque"], d["idCategoria"])
                for d in dados
            ]
        except (json.JSONDecodeError, KeyError, TypeError):
            print("Erro ao abrir produtos.json.")

    def Salvar(self):
        dados = [{
            "id": p.get_id(),
            "descricao": p.get_descricao(),
            "preco": p.get_preco(),
            "estoque": p.get_estoque(),
            "idCategoria": p.get_idCategoria()
        } for p in self.produtos]
        with open("produtos.json", "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)
