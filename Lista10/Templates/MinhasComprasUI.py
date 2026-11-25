import streamlit as st
from service_provider import obter_service

service = obter_service()

usuario = st.session_state.usuario

st.title(" Minhas compras")

pedidos = service.pedido_listar_cliente(usuario.get_id())

if not pedidos:
    st.info("Você ainda não realizou nenhuma compra.")
    st.stop()

for pedido in reversed(pedidos):

    with st.expander(
        f"Pedido #{pedido.get_id()} - "
        f"R$ {pedido.get_total():.2f}"
    ):
        st.write("Data:", pedido.get_data())
        st.write("Status:", pedido.get_status())

        st.subheader("Produtos")

        for item in pedido.get_itens():
            st.write(
                f"- {item['descricao']} | "
                f"Quantidade: {item['quantidade']} | "
                f"Preço: R$ {item['preco']:.2f}"
            )

        st.divider()

        st.write(
            f"**Total: R$ {pedido.get_total():.2f}**"
        )