import streamlit as st
from service_provider import obter_service


service = obter_service()
st.title("Cadastro de Clientes")
aba = st.radio(
    "Operação",
    ["Inserir", "Listar", "Atualizar", "Excluir"],
    horizontal=True
)
if aba == "Inserir":
    with st.form("form_cliente_inserir"):
        nome = st.text_input("Nome")
        email = st.text_input("E-mail")
        telefone = st.text_input("Telefone")
        enviar = st.form_submit_button("Cadastrar")
    if enviar:
        if not nome.strip() or not email.strip() or not telefone.strip():
            st.warning("Preencha todos os campos.")
        elif service.cliente_inserir(
            nome.strip(),
            email.strip(),
            telefone.strip()
        ):
            st.success("Cliente cadastrado com sucesso!")
        else:
            st.error("Não foi possível cadastrar o cliente.")
elif aba == "Listar":
    st.subheader("Clientes cadastrados")
    clientes = service.cliente_listar()
    if clientes:
        st.dataframe(
            [
                {
                    "ID": c.get_id(),
                    "Nome": c.get_nome(),
                    "E-mail": c.get_email(),
                    "Telefone": c.get_telefone()
                }
                for c in clientes
            ],
            width='content',
            hide_index=True
        )
    else:
        st.info("Nenhum cliente cadastrado.")
elif aba == "Atualizar":
    clientes = service.cliente_listar()
    if not clientes:
        st.info("Não existem clientes para atualizar.")
        st.stop()
    opcoes = {
        f'{c.get_id()} - {c.get_nome()}': c.get_id()
        for c in clientes
    }
    selecionada = st.selectbox(
        "Cliente",
        list(opcoes)
    )
    cliente_id = opcoes[selecionada]
    cliente = service.cliente_listar_id(cliente_id)
    with st.form("form_cliente_atualizar"):
        nome = st.text_input(
            "Nome",
            value=cliente.get_nome()
        )
        email = st.text_input(
            "E-mail",
            value=cliente.get_email()
        )
        telefone = st.text_input(
            "Telefone",
            value=cliente.get_telefone()
        )
        enviar = st.form_submit_button("Atualizar")
    if enviar:
        if not nome.strip() or not email.strip() or not telefone.strip():
            st.warning("Preencha todos os campos.")
        elif service.cliente_atualizar(
            cliente_id,
            nome.strip(),
            email.strip(),
            telefone.strip()
        ):
            st.success("Cliente atualizado com sucesso!")
        else:
            st.error("Não foi possível atualizar o cliente.")
elif aba == "Excluir":
    clientes = service.cliente_listar()
    if not clientes:
        st.info("Não existem clientes para excluir.")
        st.stop()
    opcoes = {
        f'{c.get_id()} - {c.get_nome()}': c.get_id()
        for c in clientes
    }
    selecionada = st.selectbox(
        "Cliente para excluir",
        list(opcoes)
    )
    cliente_id = opcoes[selecionada]
    if st.button("Excluir cliente", type="primary"):
        if service.cliente_excluir(cliente_id):
            st.success("Cliente excluído com sucesso!")
            st.rerun()
        else:
            st.error("Cliente não encontrado.")