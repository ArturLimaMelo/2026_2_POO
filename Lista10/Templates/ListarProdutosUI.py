import streamlit as st
from service_provider import obter_service
from CarrinhoService import CarrinhoService

service = obter_service()

st.title(" Produtos disponíveis")

produtos = service.produto_listar()
categorias = service.categoria_listar()

categorias_por_id = {
    c.get_id(): c.get_descricao()
    for c in categorias
}

if not produtos:
    st.info("Nenhum produto cadastrado.")
    st.stop()

for produto in produtos:
    if produto.get_estoque() <= 0:
        continue

    with st.container(border=True):
        col1, col2 = st.columns([3, 1])

        with col1:
            st.subheader(produto.get_descricao())

            st.write(
                "Categoria:",
                categorias_por_id.get(
                    produto.get_idCategoria(),
                    "Não encontrada"
                )
            )

            st.write(
                f"Preço: R$ {produto.get_preco():.2f}"
            )

            st.write(
                f"Estoque disponível: {produto.get_estoque()}"
            )

        with col2:
            quantidade = st.number_input(
                "Quantidade",
                min_value=1,
                max_value=produto.get_estoque(),
                value=1,
                step=1,
                key=f"quantidade_{produto.get_id()}"
            )

            if st.button(
                "Adicionar ao carrinho",
                key=f"adicionar_{produto.get_id()}",
                use_container_width=True
            ):
                CarrinhoService.adicionar(
                    produto.get_id(),
                    quantidade
                )

                st.success("Produto adicionado ao carrinho!")
                st.rerun()