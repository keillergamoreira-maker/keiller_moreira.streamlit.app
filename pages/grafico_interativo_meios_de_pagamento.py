#===Importar o Streamlit
import streamlit as st

#===Importar o módulo de carreamento do arquivo
from carregar_arquivo import carregar_arquivo

#===Importar o módulo dos gráficos
from graficos import Graficos

#===Configurações da página
st.set_page_config(
    page_title='Meios de Pagamento',
    page_icon=':bar_chart:',
    layout='wide'
)

st.write(f'**Oi** _{st.session_state.usuario}_, **é bom te ter por aqui!**')

#---Título da página
st.title('Meios de Pagamento')
st.subheader('Nesta página veremos como os cliente optam por pagar suas faturas, que pode ser por Saque Bancário, Cartão de Crédito, Cheque Enviado')
st.markdown('Pode mos verificar que:\n\n '
            '- _**55,50%**_ dos clientes preferem pagar por meio de _Saque Bancário_, totalizando _**3.909**_ clientes;\n\n '
            '- _**39,00%**_ dos clientes preferem pagar por meio de _Cartão de Crédito_, totalizando _**2.749**_ clientes;\n\n '
            '- _**5,47%**_ dos clientes preferem pagar por meio de _Cheque Enviado_, totalizando _**385**_ clientes.')

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
            options='Payment Method',
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

st.image("C:/Users/User/Documents/PÓS GESTÃO ESTRATÉGICA DE DADOS/02 - DATAVIZ COM PYTHON/PROJETOS_1/PROJETO STREAMLIT/logo_KMA.jpeg", width=1000)