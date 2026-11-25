import streamlit as st
from service_provider import obter_service


service = obter_service()
st.title("Cadastro de Categorias")
aba = st.radio(
    "Operação",
    ["Inserir", "Listar", "Atualizar", "Excluir"],
    horizontal=True
)
if aba == "Inserir":
    with st.form("form_categoria_inserir"):
        descricao = st.text_input("Descrição")
        enviar = st.form_submit_button("Cadastrar")
    if enviar:
        if not descricao.strip():
            st.warning("Informe a descrição da categoria.")
        elif service.categoria_inserir(descricao.strip()):
            st.success("Categoria cadastrada com sucesso!")
        else:
            st.error("Não foi possível cadastrar a categoria.")
elif aba == "Listar":
    st.subheader("Categorias cadastradas")
    categorias = service.categoria_listar()
    if categorias:
        st.dataframe(
            [
                {
                    "ID": c.get_id(),
                    "Descrição": c.get_descricao()
                }
                for c in categorias
            ],
            width='content',
            hide_index=True
        )
    else:
        st.info("Nenhuma categoria cadastrada.")
elif aba == "Atualizar":
    categorias = service.categoria_listar()
    if not categorias:
        st.info("Não existem categorias para atualizar.")
        st.stop()
    opcoes = {
        f'{c.get_id()} - {c.get_descricao()}': c.get_id()
        for c in categorias
    }
    selecionada = st.selectbox(
        "Categoria",
        list(opcoes)
    )
    categoria_id = opcoes[selecionada]
    categoria = service.categoria_listar_id(categoria_id)
    with st.form("form_categoria_atualizar"):
        descricao = st.text_input(
            "Nova descrição",
            value=categoria.get_descricao()
        )
        enviar = st.form_submit_button("Atualizar")
    if enviar:
        if not descricao.strip():
            st.warning("Informe a descrição.")
        elif service.categoria_atualizar(
            categoria_id,
            descricao.strip()
        ):
            st.success("Categoria atualizada com sucesso!")
        else:
            st.error("Não foi possível atualizar a categoria.")
elif aba == "Excluir":
    categorias = service.categoria_listar()
    if not categorias:
        st.info("Não existem categorias para excluir.")
        st.stop()
    opcoes = {
        f'{c.get_id()} - {c.get_descricao()}': c.get_id()
        for c in categorias
    }
    selecionada = st.selectbox(
        "Categoria para excluir",
        list(opcoes)
    )
    categoria_id = opcoes[selecionada]
    if st.button("Excluir categoria", type="primary"):
        if service.categoria_excluir(categoria_id):
            st.success("Categoria excluída com sucesso!")
            st.rerun()
        else:
            st.error("Categoria não encontrada.")