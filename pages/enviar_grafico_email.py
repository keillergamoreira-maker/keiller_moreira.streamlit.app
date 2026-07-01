#===Importar as bibliotecas
import io
import streamlit as st

#===Importar o módulo de carreamento do arquivo
from carregar_arquivo import carregar_arquivo

#===Importar o módulo dos gráficos
from graficos import Graficos

#===Importar o módulo para envio do e-mail
from enviar_email import enviar_email

#===Configurações da página
st.set_page_config(
    page_title='Enviar gráfico por email',
    page_icon=':bar_chart:',
    layout='wide'
)

st.write(f'**Oi** _{st.session_state.usuario}_, **é bom te ter por aqui!**')

#===Título da página
st.title('Enviar gráfico por email')
st.subheader('Esta página é dedicada ao envio de gráficos selecionados pelo usuário como anexos por e-mail para '
             'o destinatário desejado.')
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
        options=sorted(['Histograma', 'Pizza']),
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
            options=colunas_df,
            key='colunas_def',
            index=None
        )
#===Campos do e-mail
with st.form('email'):
    destinatario = st.text_input(
        label='Destinatario:*',
        placeholder='Digite o e-mail do destinatário',
        key='destinatário'
    )
    assunto = st.text_input(
        label='Assunto:',
        value='Envio do gráfico selecionado para análise ',
        placeholder='Digite o assunto do e-mail',
        key='assunto'
    )

    corpo = st.text_area(
        label='Corpo do e-mail:',
        placeholder='A mensagem aqui pode ser escrita normalmente',
        value='\n\nAtenciosamente,\n'
              'Keiller Moreira ',
        key='corpo'
    )
    enviar = st.form_submit_button('Enviar e-mail', width='stretch')

#===Verifivar se o botão foi clicado
if enviar:
    #===Verificar se o destinatario foi especificado
    if not destinatario:
        st.warning('Por favor, digite o e-mail do destinatário')
    else:
        with st.spinner('Preparando e enviando o e-mail...'):
            #===Salvar o grafico na memoria
            graficos = Graficos(df, colunas, True)
            buffer = io.BytesIO()

            #===Tipo do grafico
            if grafico == 'Histograma':
                histograma = graficos.histograma_estatico()
                histograma.savefig(buffer, format='png', bbox_inches='tight')
                nome_arquivo = f'histograma_{colunas}.png'

            if grafico == 'Pizza':
                pizza = graficos.pizza_estatico()
                pizza.savefig(buffer, format='png', bbox_inches='tight')
                nome_arquivo = f'pizza_{colunas}.png'

            #===Enviar o e-mail
            remetente = st.secrets['REMETENTE']
            senha = st.secrets['SENHA']
            sucesso = enviar_email(remetente, senha, destinatario, assunto,
                                    corpo, buffer, nome_arquivo)
            if sucesso:
                st.success('E-mail enviado com sucesso!')

st.image("archives/logo_KMA.jpeg", width=1000)