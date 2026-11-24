import streamlit as st
from Service import Service


@st.cache_resource
def obter_service():
    return Service()