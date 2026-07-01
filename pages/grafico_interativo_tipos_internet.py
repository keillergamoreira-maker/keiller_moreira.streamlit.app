#===Importar o Streamlit
import streamlit as st

#===Importar o módulo de carreamento do arquivo
from carregar_arquivo import carregar_arquivo

#===Importar o módulo dos gráficos
from graficos import Graficos

#===Configurações da página
st.set_page_config(
    page_title='Tecnologia de Transmissão Internet',
    page_icon=':bar_chart:',
    layout='wide'
)

st.write(f'**Oi** _{st.session_state.usuario}_, **é bom te ter por aqui!**')

#---Título da página
st.title('Tecnologia de Transmissão Internet')
st.subheader('Nesta página veremos, considerando os clientes que assinam o serviço de internet, a proporção do tipo de tecnologia que a Telco envia para os clientes, que pode ser DSL, Fibra Óptica ou Cabo.')
st.markdown('Pode mos verificar que:\n\n '
            '- _**55,00%**_ dos clientes recebem o sinal de internet por _Fibra Ótica_, totalizando _**3.035**_ clientes;\n\n '
            '- _**29,90%**_ dos clientes recebem o sinal de internet por _DSL_, totalizando _**1.652**_ clientes;\n\n '
            '- _**15,00%**_ dos clientes recebem o sinal de internet por _Cabo_, totalizando _**830**_ clientes.')

st. divider()

#---Enviar o arquivo
upload = st.file_uploader(
    label='Enviar o arquivo',
    type=['csv', 'xlsx']
)

#---Carregar o arquivo
if upload is not None:
    df = carregar_arquivo(upload)

    #---Selecionar o tipo de grafico
    grafico = st.selectbox(
        label='Selecionar o gráfico:',
        placeholder='Selecione o tipo de gráfico a ser analisado!',
        options=sorted(['Histograma', 'Pizza']),
        key='graficos',
        index=None
    )

    #---Separar as colunas numericas das categóricas
    if grafico is not None:
        if grafico in ('Histograma'):
            colunas_df = [coluna for coluna in df.columns if df[coluna].dtype != 'str']
        elif grafico == 'Pizza':
            colunas_df = [coluna for coluna in df.columns if df[coluna].dtype == 'str']

        #---Obter as colunas da tabela
        colunas = st.selectbox(
            label='Selecionar a coluna:',
            placeholder='Selecione a coluna para a criação do gráfico:',
            options='Internet Type',
            key='colunas_def',
            index=None
        )

        #----Instanciar a classe
        graficos = Graficos(df, colunas, False)

        #---Mostrar o grafico selecionado
        if colunas is not None:
            if grafico == 'Histograma':
                graficos.histograma_interativo()

            if grafico == 'Pizza':
                graficos.pizza_interativo()

st.image('archives/logo_KMA.jpeg', width=1000)