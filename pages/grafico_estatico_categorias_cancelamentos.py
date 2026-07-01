#===Importar o Streamlit
import streamlit as st

#===Importar o módulo de carreamento do arquivo
from carregar_arquivo import carregar_arquivo

#===Importar o módulo dos gráficos
from graficos import Graficos

#===Configurações da página
st.set_page_config(
    page_title='Categorias de Cancelamentos',
    page_icon=':bar_chart:',
    layout='wide'
)

st.write(f'**Oi** _{st.session_state.usuario}_, **é bom te ter por aqui!**')

#===Título da página
st.title('Categorias de Cancelamentos')
st.subheader('Nesta página veremos as categorias referentes aos motivos dos cancelamentos. Essas categorias são '
             'perguntadas aos clientes no ato do cancelamento e se referem diretamente ao motivo que o mesmo levou em '
             'consideração para cancelar seu plano. ')

st.markdown('Podemos observar que:\n\n '
            '- A maior categoria se refere ao "Concorrente" num total de _**841**_ ocorrências, representando _**45,00%**_.')


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
            options='Churn Category',
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

st.image('archives/logo_KMA.jpeg', width=1000)