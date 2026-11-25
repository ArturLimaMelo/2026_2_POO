import json
import os
from Cliente import Cliente


class ClienteDAO:
    def __init__(self):
        self.clientes = []

    def Inserir(self, cliente):
        if self.Listar_Id(cliente.get_id()) is not None:
            return False

        if self.Listar_Email(cliente.get_email()) is not None:
            return False

        self.clientes.append(cliente)
        self.Salvar()
        return True

    def Listar(self):
        return self.clientes

    def Listar_Id(self, id):
        for cliente in self.clientes:
            if cliente.get_id() == id:
                return cliente
        return None

    def Listar_Email(self, email):
        for cliente in self.clientes:
            if cliente.get_email().lower() == email.lower():
                return cliente
        return None

    def Atualizar(self, id, nome, email, telefone):
        cliente = self.Listar_Id(id)

        if cliente is None:
            return False

        outro = self.Listar_Email(email)

        if outro is not None and outro.get_id() != id:
            return False

        cliente.set_nome(nome)
        cliente.set_email(email)
        cliente.set_telefone(telefone)

        self.Salvar()
        return True

    def Excluir(self, id):
        cliente = self.Listar_Id(id)

        if cliente is None:
            return False

        self.clientes.remove(cliente)
        self.Salvar()
        return True

    def Abrir(self):
        if not os.path.exists("clientes.json"):
            return

        try:
            with open("clientes.json", "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)

            self.clientes = [
                Cliente(
                    d["id"],
                    d["nome"],
                    d["email"],
                    d["telefone"],
                    salt=d.get("salt"),
                    senha_hash=d.get("senha_hash")
                )
                for d in dados
            ]

        except (json.JSONDecodeError, KeyError, TypeError):
            print("Erro ao abrir clientes.json.")

    def Salvar(self):
        dados = [
            {
                "id": c.get_id(),
                "nome": c.get_nome(),
                "email": c.get_email(),
                "telefone": c.get_telefone(),
                "salt": c.get_salt(),
                "senha_hash": c.get_senha_hash()
            }
            for c in self.clientes
        ]

        with open("clientes.json", "w", encoding="utf-8") as arquivo:
            json.dump(
                dados,
                arquivo,
                ensure_ascii=False,
                indent=4
            )