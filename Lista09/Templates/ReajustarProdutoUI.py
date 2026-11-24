import streamlit as st
from service_provider import obter_service


service = obter_service()
st.title("Reajustar Preços dos Produtos")
produtos = service.produto_listar()
if not produtos:
    st.info(
        "Não existem produtos cadastrados para reajustar."
    )
    st.stop()
st.subheader("Preços atuais")
st.dataframe(
    [
        {
            "ID": p.get_id(),
            "Produto": p.get_descricao(),
            "Preço atual (R$)": f'{p.get_preco():.2f}'
        }
        for p in produtos
    ],
    width='content',
    hide_index=True
)
with st.form("form_reajuste"):
    percentual = st.number_input(
        "Percentual de reajuste",
        value=0.0,
        step=1.0,
        help=(
            "Use um valor positivo para aumento "
            "e negativo para redução."
        )
    )
    enviar = st.form_submit_button("Aplicar reajuste")
if enviar:
    if percentual <= -100:
        st.error(
            "O percentual não pode ser igual ou inferior a -100%."
        )
    elif service.produto_reajustar(percentual):
        st.success(
            f"Preços reajustados em {percentual:.2f}% com sucesso!"
        )
        st.rerun()
    else:
        st.error("Não foi possível reajustar os preços.")