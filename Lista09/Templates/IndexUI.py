import streamlit as st

from ManterCategoriaUI import ManterCategoriaUI
from ManterClienteUI import ManterClienteUI
from ManterProdutoUI import ManterProdutoUI
from ReajustarProdutoUI import ReajustarProdutoUI


st.set_page_config(
    page_title="Sistema de Gerenciamento",
    page_icon="🛒",
    layout="wide"
)


st.title("Sistema de Gerenciamento")
st.subheader("Operações disponíveis")
col1, col2 = st.columns(2)
with col1:
    st.info(
        "Cadastro, consulta, atualização e exclusão de clientes."
    )
    st.info(
        "Cadastro, consulta, atualização e exclusão de categorias."
    )
with col2:
    st.info(
        "Cadastro, consulta, atualização e exclusão de produtos."
    )
    st.info(
        "Reajuste percentual dos preços dos produtos."
    )