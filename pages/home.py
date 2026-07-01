#===Importar o Streamlit
import streamlit as st

#===Configurações da página
st.set_page_config(
    page_title='Análise Telco - Página Inicial',
    page_icon=':bar_chart:',
    layout='wide'
)

#===Título da página
st.title('Análise de Operação Telco')

#===Descrição da página
st.subheader('Neste site iremos analisar o portifólio de assinaturas do cliente Telco.')

st.markdown('Objetivos da análise:\n\n'
            '- O foco principal será nos cancelamentos e seus respectivos motivos;\n\n'
            '- Outros resultados, pertinente ao desempenho da empresa, também serão avaliados;\n\n'
            '- Relatório final com análise e diagnóstico dos resultados.')

#---Salvar informações na sessão
if 'usuario' not in st.session_state:
    st.session_state.usuario = None

#---Usar a sidebar para fazer o login
usuario = st.sidebar.text_input(
    label='Usuário:',
    placeholder='Digite o nome de usuário'
)

senha = st.sidebar.text_input(
    label='Senha:',
    placeholder='Digite a senha',
    type='password'
)

if st.sidebar.button('Login', width='stretch'):
    if senha == '1234':
         st.session_state.usuario = usuario
         st.sidebar.success('Login realizado com sucesso!')
    else:
         st.sidebar.warning('Usuário não cadastrado.')

st.image('archives/logo_KMA.jpeg', width=1000)