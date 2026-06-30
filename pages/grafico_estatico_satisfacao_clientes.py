#===Importar o Streamlit
import streamlit as st

#===Importar o módulo de carreamento do arquivo
from carregar_arquivo import carregar_arquivo

#===Importar o módulo dos gráficos
from graficos import Graficos

#===Configurações da página
st.set_page_config(
    page_title='Índice de Satisfação',
    page_icon=':bar_chart:',
    layout='wide'
)

st.write(f'**Oi** _{st.session_state.usuario}_, **é bom te ter por aqui!**')

#===Título da página
st.title('Índice de Satisfação')
st.subheader('Nesta página será apresentada o nível de satisfação dos clientes para com a prestação de serviços '
             'da Telco. Este índice é medido considerando 1 (Muito Insatisfeito) a 5 (Muito Satisfeito).')

st.markdown('Podemos observar que:\n\n '
            '- Apenas _**16,30%**_ dos clientes se consideram _Muito Satisfeito_ com a prestação de serviços da Telco;\n\n '
            '- A maior parte dos clientes deu nota 3, representando _**37,80%**_ do total de avaliações, o que podemos'
            ' considera-los como uma percepção de satisfação média perante os serviçoes prestados pela Telco.\n\n '
            '- Somando os clientes que deram nota 1, 2 ou 3, temos _**58,30%**_ considerando os serviços da Telco de '
            'médio para muito insatisfeito.')

st. divider()

#===Enviar o arquivo
upload = st.file_uploader(
    label='Enviar o arquivo',
    type=['csv', 'xlsx']
)

#===Carregar o arquivo
if upload is not None:
    df = carregar_arquivo(upload)

    #===Selecionar o tipo de grafico
    grafico = st.selectbox(
        label='Selecionar o gráfico:',
        placeholder='Selecione o tipo de gráfico a ser analisado!',
        options=(['Pizza','Histograma']),
        key='graficos',
        index=None
    )

    #===Separar as colunas numericas das categóricas
    if grafico is not None:
        if grafico in ('Histograma'):
            colunas_df = [coluna for coluna in df.columns if df[coluna].dtype != 'str']
        elif grafico == 'Pizza':
            colunas_df = [coluna for coluna in df.columns if df[coluna].dtype == 'str']

        #===Obter as colunas da tabela
        colunas = st.selectbox(
            label='Selecionar a coluna:',
            placeholder='Selecione a coluna para a criação do gráfico:',
            options='Satisfaction Score',
            key='colunas_def',
            index=None
        )

        #===Instanciar a classe
        graficos = Graficos(df, colunas, False)

        #===Mostrar o grafico selecionado
        if colunas is not None:
            if grafico == 'Histograma':
                graficos.histograma_estatico()

            if grafico == 'Pizza':
                graficos.pizza_estatico()

st.image("C:/Users/User/Documents/PÓS GESTÃO ESTRATÉGICA DE DADOS/02 - DATAVIZ COM PYTHON/PROJETOS_1/PROJETO STREAMLIT/logo_KMA.jpeg", width=1000)