import streamlit as st
from service_provider import obter_service


service = obter_service()
st.title("Cadastro de Produtos")
aba = st.radio(
    "Operação",
    ["Inserir", "Listar", "Atualizar", "Excluir"],
    horizontal=True
)
categorias = service.categoria_listar()
if aba == "Inserir":
    if not categorias:
        st.warning(
            "Cadastre uma categoria antes de inserir produtos."
        )
        st.stop()
    opcoes_categoria = {
        f'{c.get_id()} - {c.get_descricao()}': c.get_id()
        for c in categorias
    }
    with st.form("form_produto_inserir"):
        descricao = st.text_input("Descrição")
        preco = st.number_input(
            "Preço (R$)",
            min_value=0.0,
            step=0.5
        )
        estoque = st.number_input(
            "Estoque",
            min_value=0,
            step=1,
            value=0
        )
        categoria = st.selectbox(
            "Categoria",
            list(opcoes_categoria)
        )
        enviar = st.form_submit_button("Cadastrar")
    if enviar:
        if not descricao.strip():
            st.warning("Informe a descrição do produto.")
        elif service.produto_inserir(
            descricao.strip(),
            preco,
            estoque,
            opcoes_categoria[categoria]
        ):
            st.success("Produto cadastrado com sucesso!")
        else:
            st.error("Não foi possível cadastrar o produto.")
elif aba == "Listar":
    st.subheader("Produtos cadastrados")
    produtos = service.produto_listar()
    if produtos:
        categorias_por_id = {
            c.get_id(): c.get_descricao()
            for c in categorias
        }
        st.dataframe(
            [
                {
                    "ID": p.get_id(),
                    "Descrição": p.get_descricao(),
                    "Preço (R$)": f'{p.get_preco():.2f}',
                    "Estoque": p.get_estoque(),
                    "Categoria": categorias_por_id.get(
                        p.get_idCategoria(),
                        "Categoria não encontrada"
                    )
                }
                for p in produtos
            ],
            width='content',
            hide_index=True
        )
    else:
        st.info("Nenhum produto cadastrado.")
elif aba == "Atualizar":
    produtos = service.produto_listar()
    if not produtos:
        st.info("Não existem produtos para atualizar.")
        st.stop()
    if not categorias:
        st.warning(
            "Cadastre uma categoria antes de atualizar produtos."
        )
        st.stop()
    opcoes_produto = {
        f'{p.get_id()} - {p.get_descricao()}': p.get_id()
        for p in produtos
    }
    selecionada = st.selectbox(
        "Produto",
        list(opcoes_produto)
    )
    produto_id = opcoes_produto[selecionada]
    produto = service.produto_listar_id(produto_id)
    opcoes_categoria = {
        f'{c.get_id()} - {c.get_descricao()}': c.get_id()
        for c in categorias
    }
    categoria_atual = next(
        (
            nome
            for nome, cid in opcoes_categoria.items()
            if cid == produto.get_idCategoria()
        ),
        list(opcoes_categoria)[0]
    )
    with st.form("form_produto_atualizar"):
        descricao = st.text_input(
            "Descrição",
            value=produto.get_descricao()
        )
        preco = st.number_input(
            "Preço (R$)",
            min_value=0.0,
            value=float(produto.get_preco()),
            step=0.5
        )
        estoque = st.number_input(
            "Estoque",
            min_value=0,
            value=int(produto.get_estoque()),
            step=1
        )
        categoria = st.selectbox(
            "Categoria",
            list(opcoes_categoria),
            index=list(opcoes_categoria).index(categoria_atual)
        )
        enviar = st.form_submit_button("Atualizar")
    if enviar:
        if not descricao.strip():
            st.warning("Informe a descrição do produto.")
        elif service.produto_atualizar(
            produto_id,
            descricao.strip(),
            preco,
            estoque,
            opcoes_categoria[categoria]
        ):
            st.success("Produto atualizado com sucesso!")
        else:
            st.error("Não foi possível atualizar o produto.")
elif aba == "Excluir":
    produtos = service.produto_listar()
    if not produtos:
        st.info("Não existem produtos para excluir.")
        st.stop()
    opcoes = {
        f'{p.get_id()} - {p.get_descricao()}': p.get_id()
        for p in produtos
    }
    selecionada = st.selectbox(
        "Produto para excluir",
        list(opcoes)
    )
    produto_id = opcoes[selecionada]
    if st.button("Excluir produto", type="primary"):
        if service.produto_excluir(produto_id):
            st.success("Produto excluído com sucesso!")
            st.rerun()
        else:
            st.error("Produto não encontrado.")