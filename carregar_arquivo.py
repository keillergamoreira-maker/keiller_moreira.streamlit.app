#===Importar as bibliotecas

import numpy as np
import pandas as pd
import streamlit as st


#@st.cache_data(show_spinner='Abrindo arquivo...')
def carregar_arquivo(upload):
    """Função responsável por carregar o arquivo de upload e mostrar no site a tabela."""
    #---Verificar qual tipo de arquivo foi verificado
    if '.csv' in upload.name:
        df = pd.read_csv(upload)
    if '.xlsx' in upload.name:
        df = pd.read_excel(upload)

    return df