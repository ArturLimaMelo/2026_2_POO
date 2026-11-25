import streamlit as st
from service_provider import obter_service

service = obter_service()

st.title(" Vendas realizadas")

pedidos = service.pedido_listar()

if not pedidos:
    st.info("Nenhuma venda realizada.")
    st.stop()

dados = []

for pedido in pedidos:
    dados.append({
        "Pedido": pedido.get_id(),
        "Cliente": pedido.get_nome_cliente(),
        "ID do cliente": pedido.get_id_cliente(),
        "Data": pedido.get_data(),
        "Total (R$)": f"{pedido.get_total():.2f}",
        "Status": pedido.get_status()
    })

st.dataframe(
    dados,
    width='content',
    hide_index=True
)

st.divider()

st.subheader("Detalhes das vendas")

for pedido in reversed(pedidos):

    with st.expander(f"Pedido #{pedido.get_id()}"):

        st.write("Cliente:", pedido.get_nome_cliente())
        st.write("Data:", pedido.get_data())

        for item in pedido.get_itens():
            st.write(
                f"- {item['descricao']} | "
                f"{item['quantidade']} unidade(s) | "
                f"R$ {item['preco']:.2f}"
            )

        st.write(
            f"**Total: R$ {pedido.get_total():.2f}**"
        )