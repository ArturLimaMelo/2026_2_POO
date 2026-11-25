import streamlit as st
from service_provider import obter_service

service = obter_service()

st.title(" Abrir conta")
st.write("Cadastre-se para comprar produtos.")

with st.form("form_cadastro"):
    nome = st.text_input("Nome")
    email = st.text_input("E-mail")
    telefone = st.text_input("Telefone")
    senha = st.text_input("Senha", type="password")
    confirmar_senha = st.text_input(
        "Confirmar senha",
        type="password"
    )

    cadastrar = st.form_submit_button(
        "Criar conta",
        use_container_width=True
    )

if cadastrar:
    if not nome.strip() or not email.strip():
        st.warning("Preencha o nome e o e-mail.")

    elif not telefone.strip() or not senha:
        st.warning("Preencha todos os campos.")

    elif senha != confirmar_senha:
        st.error("As senhas não coincidem.")

    elif len(senha) < 6:
        st.warning("A senha deve possuir pelo menos 6 caracteres.")

    elif service.cadastrar_cliente(
        nome,
        email,
        telefone,
        senha
    ):
        st.success("Conta criada com sucesso!")
        st.info("Agora você pode entrar no sistema.")
        st.page_link("LoginUI.py", label="Ir para o login")

    else:
        st.error(
            "Não foi possível criar a conta. "
            "Verifique se o e-mail já está cadastrado."
        )

st.divider()

st.page_link(
    "LoginUI.py",
    label="Voltar para o login"
)