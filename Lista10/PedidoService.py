from Pedido import Pedido
from CarrinhoService import CarrinhoService


class PedidoService:

    def __init__(self, service):
        self.service = service

    def confirmar_compra(self, cliente):
        carrinho = CarrinhoService.obter_carrinho()

        if not carrinho:
            return False, "O carrinho está vazio."

        itens = []


        for produto_id, quantidade in carrinho.items():

            produto = self.service.produto_listar_id(produto_id)

            if produto is None:
                return False, "Um produto do carrinho não existe mais."

            if quantidade <= 0:
                return False, "Quantidade inválida."

            if produto.get_estoque() < quantidade:
                return False, (
                    f"Estoque insuficiente para "
                    f"{produto.get_descricao()}."
                )

            itens.append({
                "produto_id": produto.get_id(),
                "descricao": produto.get_descricao(),
                "preco": produto.get_preco(),
                "quantidade": quantidade
            })


        pedidos = self.service.pedido_listar()

        pedido_id = (
            max((p.get_id() for p in pedidos), default=0) + 1
        )

        pedido = Pedido(
            pedido_id,
            cliente.get_id(),
            cliente.get_nome(),
            itens
        )


        for item in itens:
            produto = self.service.produto_listar_id(
                item["produto_id"]
            )

            novo_estoque = (
                produto.get_estoque() - item["quantidade"]
            )

            self.service.produto_atualizar(
                produto.get_id(),
                produto.get_descricao(),
                produto.get_preco(),
                novo_estoque,
                produto.get_idCategoria()
            )


        if not self.service.pedido_inserir(pedido):
            return False, "Não foi possível registrar o pedido."

        CarrinhoService.limpar()

        return True, pedido