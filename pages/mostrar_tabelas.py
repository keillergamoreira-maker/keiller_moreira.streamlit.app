#===Importar o Streamlit

import streamlit as st

#===Importar o modulo de carregamento de tabelas
from carregar_arquivo import carregar_arquivo

st.write(f'**Oi** _{st.session_state.usuario}_, **é bom te ter por aqui!**')

#===Configurações da página
st.set_page_config(
    page_title='Análise Telco - Tabelas',
    page_icon=':bar_chart:',
    layout='wide'
)

#===Título da página
st.title('Tabela Resultados Telco')
st.subheader('Nesta página, será apresentada a tabela apresentando todos os resultados obtidos e coletados pela '
                 'Telco no período de análise.')


#===Carregar arquivos
upload = st.file_uploader(
    label='Enviar arquivos:',
    type=['csv', 'xlsx']
    )

#===Carregar o arquivo conforme o tipo de arquivo
if upload is not None:
    df = carregar_arquivo(upload)
    st.dataframe(df)

st.image("C:/Users/User/Documents/PÓS GESTÃO ESTRATÉGICA DE DADOS/02 - DATAVIZ COM PYTHON/PROJETOS_1/PROJETO STREAMLIT/logo_KMA.jpeg", width=1000)