import streamlit as st

st.title("Sistema de Comércio Eletrônico")

st.subheader("Painel administrativo")

st.write(
    "Bem-vindo ao sistema de gerenciamento do comércio eletrônico."
)

col1, col2 = st.columns(2)

with col1:
    st.info(
        " **Clientes**\n\n"
        "Gerencie os clientes cadastrados."
    )

    st.info(
        " **Categorias**\n\n"
        "Cadastre, consulte, atualize e exclua categorias."
    )

    st.info(
        " **Produtos**\n\n"
        "Gerencie os produtos disponíveis na loja."
    )

with col2:
    st.info(
        " **Reajustar preços**\n\n"
        "Aplique reajustes percentuais aos produtos."
    )

    st.info(
        " **Vendas**\n\n"
        "Consulte os pedidos realizados pelos clientes."
    )