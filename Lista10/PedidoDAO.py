import json
import os
from Pedido import Pedido


class PedidoDAO:
    def __init__(self):
        self.pedidos = []

    def Inserir(self, pedido):
        if self.Listar_Id(pedido.get_id()) is not None:
            return False

        self.pedidos.append(pedido)
        self.Salvar()
        return True

    def Listar(self):
        return self.pedidos

    def Listar_Id(self, id):
        for pedido in self.pedidos:
            if pedido.get_id() == id:
                return pedido
        return None

    def Listar_Cliente(self, id_cliente):
        return [
            pedido for pedido in self.pedidos
            if pedido.get_id_cliente() == id_cliente
        ]

    def Abrir(self):
        if not os.path.exists("pedidos.json"):
            return

        try:
            with open("pedidos.json", "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)

            self.pedidos = [
                Pedido(
                    d["id"],
                    d["id_cliente"],
                    d["nome_cliente"],
                    d["itens"],
                    d["data"],
                    d["status"]
                )
                for d in dados
            ]

        except (json.JSONDecodeError, KeyError, TypeError):
            print("Erro ao abrir pedidos.json.")

    def Salvar(self):
        dados = [
            {
                "id": p.get_id(),
                "id_cliente": p.get_id_cliente(),
                "nome_cliente": p.get_nome_cliente(),
                "itens": p.get_itens(),
                "data": p.get_data(),
                "status": p.get_status()
            }
            for p in self.pedidos
        ]

        with open("pedidos.json", "w", encoding="utf-8") as arquivo:
            json.dump(
                dados,
                arquivo,
                ensure_ascii=False,
                indent=4
            )