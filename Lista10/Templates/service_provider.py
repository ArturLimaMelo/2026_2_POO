import streamlit as st
from Service import Service
from PedidoService import PedidoService


@st.cache_resource
def obter_service():
    return Service()


@st.cache_resource
def obter_pedido_service():
    return PedidoService(obter_service())