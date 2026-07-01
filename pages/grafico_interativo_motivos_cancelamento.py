#===Importar o Streamlit
import streamlit as st

#===Importar o módulo de carreamento do arquivo
from carregar_arquivo import carregar_arquivo

#===Importar o módulo dos gráficos
from graficos import Graficos

#===Configurações da página
st.set_page_config(
    page_title='Motivos de Cancelamentos',
    page_icon=':bar_chart:',
    layout='wide'
)

st.write(f'**Oi** _{st.session_state.usuario}_, **é bom te ter por aqui!**')

#---Título da página
st.title('Motivos de Cancelamentos')
st.subheader('Nesta página veremos por meio dos gráficos de pizza e histograma os motivos que levaram os clientes a '
             'cancelarem seus planos.')
st.markdown('Os cinco maiores motivos relatados pelos clientes, considerando os dados nulos, foram:\n\n '
            '- 1º-Concorrente ofereceu aparelhos melhores - _**313**_ ocorrências representando _**16,70%**_;\n\n '
            '- 2º-Concorrente fez uma oferta melhor - _**311**_ ocorrências representando _**16,60%**_;\n\n '
            '- 3º-Atitude do atendente de suporte - _**220**_ ocorrências representando _**11,80%**_;\n\n '
            '- 4º-Cliente não soube explicar o motivo - _**130**_ ocorrências representando _**6,96%**_;\n\n '
            '- 5º-Concorrente ofereceu mais dados - _**117**_ ocorrências representando _**6,26%**_.')

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
            options='Churn Reason',
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