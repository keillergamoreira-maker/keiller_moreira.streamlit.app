#===Importar o Streamlit
import streamlit as st

#===Importar o módulo de carreamento do arquivo
from carregar_arquivo import carregar_arquivo

#===Importar o módulo dos gráficos
from graficos import Graficos

#===Configurações da página
st.set_page_config(
    page_title='Indicações de Clientes',
    page_icon=':bar_chart:',
    layout='wide'
)

st.write(f'**Oi** _{st.session_state.usuario}_, **é bom te ter por aqui!**')

#---Título da página
st.title('Indicações de Clientes')
st.subheader('Nesta página veremos como está o nível de indicações que os clientes da Telco têm feito para algum conhecido.')
st.markdown('Pode mos verificar que:\n\n '
            '- _**54,30%**_ dos clientes não fizeram nenhuma indicação, totalizando _**3.821**_ clientes;\n\n '
            '- _**15,40%**_ dos clientes fizeram 1 indicação, totalizando _**1.086**_ clientes;\n\n '
            '- _**3,41%**_ foi a média para os clientes que fizeram 2, 3, 4, 5, 6, 7, 8, 9 ou 10 indicações. totalizando _**2.134**_ clientes;\n\n '
            '- E apenas _**0,03%**_ dos clientes fizeram 11 indicações, totalizando 8 clientes.')

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
            options='Number of Referrals',
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