import streamlit as st
from service_provider import obter_service

service = obter_service()

st.title("Comércio Eletrônico")
st.subheader("Entrar no sistema")

with st.form("form_login"):
    email = st.text_input("E-mail")
    senha = st.text_input("Senha", type="password")

    entrar = st.form_submit_button(
        "Entrar",
        use_container_width=True
    )

if entrar:
    if not email.strip() or not senha:
        st.warning("Informe o e-mail e a senha.")
    else:
        usuario = service.autenticar(email, senha)

        if usuario is None:
            st.error("E-mail ou senha incorretos.")
        else:
            st.session_state.usuario = usuario

            if usuario.get_email().lower() == "admin":
                st.session_state.perfil = "admin"
            else:
                st.session_state.perfil = "cliente"

            st.rerun()

st.divider()

st.write("Ainda não possui uma conta?")
st.page_link(
    "CadastroUI.py",
    label="Criar uma conta",
    icon=""
)