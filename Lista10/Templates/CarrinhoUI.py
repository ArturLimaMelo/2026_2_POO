import streamlit as st
from service_provider import obter_service, obter_pedido_service
from CarrinhoService import CarrinhoService

service = obter_service()
pedido_service = obter_pedido_service()

usuario = st.session_state.usuario

st.title(" Meu carrinho")

carrinho = CarrinhoService.obter_carrinho()

if not carrinho:
    st.info("Seu carrinho está vazio.")
    st.stop()

total = 0

for produto_id, quantidade in list(carrinho.items()):

    produto = service.produto_listar_id(produto_id)

    if produto is None:
        CarrinhoService.remover(produto_id)
        continue

    subtotal = produto.get_preco() * quantidade
    total += subtotal

    with st.container(border=True):
        col1, col2, col3 = st.columns([3, 2, 1])

        with col1:
            st.subheader(produto.get_descricao())
            st.write(f"Preço unitário: R$ {produto.get_preco():.2f}")

        with col2:
            nova_quantidade = st.number_input(
                "Quantidade",
                min_value=1,
                max_value=max(1, produto.get_estoque()),
                value=min(quantidade, max(1, produto.get_estoque())),
                key=f"carrinho_{produto_id}"
            )

            if nova_quantidade != quantidade:
                CarrinhoService.alterar_quantidade(
                    produto_id,
                    nova_quantidade
                )
                st.rerun()

        with col3:
            st.write(f"Subtotal: R$ {subtotal:.2f}")

            if st.button(
                "Remover",
                key=f"remover_{produto_id}"
            ):
                CarrinhoService.remover(produto_id)
                st.rerun()

st.divider()

st.subheader(f"Total: R$ {total:.2f}")

if st.button(
    "Confirmar compra",
    type="primary",
    use_container_width=True
):
    sucesso, resultado = pedido_service.confirmar_compra(usuario)

    if sucesso:
        st.success(
            f"Compra realizada! Número do pedido: {resultado.get_id()}"
        )
        st.rerun()
    else:
        st.error(resultado)