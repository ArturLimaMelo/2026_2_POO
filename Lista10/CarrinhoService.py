import streamlit as st


class CarrinhoService:

    @staticmethod
    def obter_carrinho():
        if "carrinho" not in st.session_state:
            st.session_state.carrinho = {}

        return st.session_state.carrinho

    @staticmethod
    def adicionar(produto_id, quantidade=1):
        carrinho = CarrinhoService.obter_carrinho()

        carrinho[produto_id] = (
            carrinho.get(produto_id, 0) + quantidade
        )

    @staticmethod
    def remover(produto_id):
        carrinho = CarrinhoService.obter_carrinho()

        if produto_id in carrinho:
            del carrinho[produto_id]

    @staticmethod
    def alterar_quantidade(produto_id, quantidade):
        carrinho = CarrinhoService.obter_carrinho()

        if quantidade <= 0:
            CarrinhoService.remover(produto_id)
        elif produto_id in carrinho:
            carrinho[produto_id] = quantidade

    @staticmethod
    def limpar():
        st.session_state.carrinho = {}

    @staticmethod
    def quantidade_itens():
        carrinho = CarrinhoService.obter_carrinho()

        return sum(carrinho.values())