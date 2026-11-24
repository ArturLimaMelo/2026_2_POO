import streamlit as st

paginas = {
    "": [
        st.Page("IndexUI.py", title="Inicio"),
        st.Page("ManterClienteUI.py", title="Clientes"),
        st.Page("ManterCategoriaUI.py", title="Categorias"),
        st.Page("ManterProdutoUI.py", title="Produtos"),
        st.Page("ReajustarProdutoUI.py", title="Reajustar Produtos")
    ]
}
    
pg = st.navigation(paginas)


pg.run()