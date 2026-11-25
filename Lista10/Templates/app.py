import streamlit as st
from service_provider import obter_service

st.set_page_config(
    page_title="Comércio Eletrônico",
    page_icon="",
    layout="wide"
)

service = obter_service()

if "usuario" not in st.session_state:
    st.session_state.usuario = None

if "perfil" not in st.session_state:
    st.session_state.perfil = None


if st.session_state.usuario is None:

    paginas = [
        st.Page(
            "LoginUI.py",
            title="Entrar",
            icon="",
            default=True
        ),
        st.Page(
            "CadastroUI.py",
            title="Abrir conta",
            icon=""
        )
    ]

    pg = st.navigation(paginas)
    pg.run()


else:
    usuario = st.session_state.usuario
    perfil = st.session_state.perfil

    st.sidebar.title("Comércio Eletrônico")

    st.sidebar.write(
        f"Usuário: **{usuario.get_nome()}**"
    )

    st.sidebar.write(
        f"Perfil: **{perfil.capitalize()}**"
    )

    if st.sidebar.button(
        "Sair do sistema",
        use_container_width=True
    ):
        st.session_state.usuario = None
        st.session_state.perfil = None
        st.session_state.pop("carrinho", None)
        st.rerun()


    if perfil == "admin":

        paginas = {
            "Administração": [
                st.Page(
                    "IndexUI.py",
                    title="Início",
                    icon="",
                    default=True
                ),
                st.Page(
                    "ManterClienteUI.py",
                    title="Clientes",
                    icon=""
                ),
                st.Page(
                    "ManterCategoriaUI.py",
                    title="Categorias",
                    icon=""
                ),
                st.Page(
                    "ManterProdutoUI.py",
                    title="Produtos",
                    icon=""
                ),
                st.Page(
                    "ReajustarProdutoUI.py",
                    title="Reajustar preços",
                    icon=""
                ),
                st.Page(
                    "ListarVendasUI.py",
                    title="Vendas",
                    icon=""
                )
            ]
        }


    else:

        paginas = {
            "Loja": [
                st.Page(
                    "ListarProdutosUI.py",
                    title="Produtos",
                    icon="",
                    default=True
                ),
                st.Page(
                    "CarrinhoUI.py",
                    title="Meu carrinho",
                    icon=""
                ),
                st.Page(
                    "MinhasComprasUI.py",
                    title="Minhas compras",
                    icon=""
                )
            ]
        }

    pg = st.navigation(paginas)
    pg.run()