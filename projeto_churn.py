#===Importar o Streamlit
import streamlit as st

#===Páginas de navegação
pg = st.navigation(
    [
        st.Page('./pages/home.py', title='Página Inicial'),
        st.Page('./pages/mostrar_tabelas.py', title='Tabelas - Dados Gerais'),
        st.Page('./pages/grafico_estatico_numero_cancelamentos.py', title='Número de Cancelamentos'),
        st.Page('./pages/grafico_estatico_categorias_cancelamentos.py', title='Categorias de Cancelamentos'),
        st.Page('./pages/grafico_estatico_satisfacao_clientes.py', title='Índice de Satisfação'),
        st.Page('./pages/enviar_grafico_email.py', title='Enviar gráfico por e_mail'),
        st.Page('./pages/grafico_interativo_motivos_cancelamento.py', title='Motivos de Cancelamentos'),
        st.Page('./pages/grafico_interativo_tipos_contratos.py', title='Tipos de Contratos'),
        st.Page('./pages/grafico_interativo_meios_de_pagamento.py', title='Meio de Pagamento'),
        st.Page('./pages/grafico_interativo_servico_internet.py', title='Serviço de Internet'),
        st.Page('./pages/grafico_interativo_tipos_internet.py', title='Tecnologia de Transmissão Internet'),
        st.Page('./pages/grafico_interativo_tempo_cliente.py', title='Tempo do Cliente'),
        st.Page('./pages/grafico_interativo_indicacoes.py', title='Indicações de Clientes'),
        st.Page('./pages/baixar_arquivo.py', title='Análise Final e Download do Relatório')
    ]
)

pg.run()