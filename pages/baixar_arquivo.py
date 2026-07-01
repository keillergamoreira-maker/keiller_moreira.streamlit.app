#===Importar o Streamlit
import streamlit as st

#===Importar o modulo do carregamento do arquivo
from carregar_arquivo import carregar_arquivo

#===Configuração da página
st.set_page_config(
    page_title='Análise Final e Download do Relatório',
    page_icon=':bar_chart:',
    layout='wide'
)

st.write(f'**Oi** _{st.session_state.usuario}_, **é bom te ter por aqui!**')

#===Titulo da página
st.title('Análise Final e Download do Relatório')
st.subheader('Nesta página traremos a análise final em cima dos resultados encontrados, além de sujestões e pontos de melhorias propostos para a empresa.\n\n '
             'Abaixo segue o relatório com toda a análise feita, sendo possível fazer o download do mesmo caso o usuário queira.')
st.markdown('**Análise dos Resultados**\n\n'  
            '- Mediante a avalição dos resultados foi possível identificar que a Telco perdeu 26,50% de sua \n'
            'carteira de clientes no período de análise. É uma perca significativa e além de ser drástica \n'
            'e ruptiva, pensando em níveis de faturamento e pretensões de expansão de áreas de atuação.\n\n'
            '- Avaliando mais precisamente os cancelamentos, foi possível detectar uma grande influência da \n'
            'concorrência nesse cenário de queda. Entre as categorias elencadas pelos clientes que \n'
            'efetuaram o cancelamento de seus planos, 45,00% deles afirmaram terem cancelado devido a \n'
            'ação dos concorrentes.\n\n'
            '- Dentre os cinco maiores motivos relatados pelos clientes, que os motivaram a cancelarem seus \n'
            'vínculos com a Telco, três deles estão diretamente ligados a investida dos concorrentes, que \n'
            'seriam: concorrente ofereceu melhores aparelhos, concorrente fez uma oferta melhor e \n'
            'concorrente ofereceu mais dados. Ainda entre os cinco maiores motivos, também merece \n'
            'destaque a atitude do atendente de suporte no atendimento ao cliente, motivo este que se \n'
            'refere diretamente como a Telco reporta a seus clientes.\n\n'
            '- Quanto ao índice de satisfação podemos perceber também um cenário de muita atenção para \n'
            'a empresa. Menos de 20% dos clientes se consideram “Muito Satisfeito” com os serviços \n'
            'prestados pela Telco, exatos 16,30%. Nessa avaliação checamos que quase 60,00% dos clientes \n'
            'possui um nível de satisfação de médio a pouco satisfeito, o que cria um ambiente de muito \n'
            'alerta para a empresa.\n\n'
            '- Avaliando os tipos de contratos, foi possível verificar que 51,30% dos clientes fecham seus \n'
            'planos mês a mês. Quanto aos meios de pagamento, os números são positivos com 55,50% \n'
            'sendo por meio de saque bancário e 39,00% por cartão de credito, dois meios de pagamento \n'
            'bastante seguros.\n\n'
            '- Sobre a prestação de serviço do pacote de internet, os números também são satisfatórios com \n'
            '78,30% dos clientes assinando esse serviço. Já quanto a transmissão do sinal desse serviço, \n'
            '55,00% se da por meio de fibra ótica, 29,90% por DSL e 15,00% por cabo.\n\n'
            '- Por fim, a respeito do tempo do cliente na empresa, destaque para a faixa de 32,58% dos \n'
            'clientes com 1 ano ou menos e os clientes mais antigos que se enquadram na faixa de 5 a 6 \n'
            'anos representam apenas 18,90%. Quanto as indicações, os resultados impressionam. 54,30% \n'
            'dos clientes não fizeram nenhuma indicação dos serviços da empresa.\n\n'
            '**Sugestão de melhorias**\n\n'
            '- Fica evidente o quanto ação dos concorrentes está sendo incisiva na queda no número de \n'
            'clientes. Frente a isso seria interessante a empresa rever a oferta de seus aparelhos para seus \n'
            'clientes, dando opção também para aparelhos de última geração e sempre se mantendo \n'
            'atualizada com as tendências de mercado. Seria importante rever a política de preços e pacote \n'
            'de dados para que possam ser mais atrativos e vantajoso para os clientes que optarem pelo \n'
            'serviço da empresa.\n\n'
            '- Um grande ponto de atenção seria quanto ao atendimento aos clientes. Reforçado como um \n'
            'dos principais motivos de cancelamento, somado ao baixo índice de satisfação dos clientes e \n'
            'alto índice de não indicação dos serviços da empresa pelos clientes, obtidos na análise dos \n'
            'dados, é de suma importância que a empresa reveja a questão de treinamento e qualificação \n'
            'de seu pessoal para que seu quadro de colaboradores seja apto a prestar toda assistência aos \n'
            'clientes. Com isso seria possível em melhorar o tempo de contrato dos clientes, saindo de ‘mês \n'
            'a mês’ para 1 ano ou mais e dessa forma traria mais previsibilidade de médio e longo prazo \n'
            'quanto a captação de receitas e faturamento, pois maiores tempos de contratos trazem mais \n'
            'estabilidade e segurança para a empresa.\n\n'
            '- E por último, seria interessante a empresa buscar uma meta de médio a longo prazo para a \n'
            'transição de 100,00% de seu sinal de internet ser enviado via fibra ótica para seus clientes. \n'
            'Apesar de exigir uma infraestrutura e investimentos mais altos, o valor agregado cobrado pelo \n'
            'serviço, além de ser uma tecnologia bem mais avançada, podem garantir maiores lucros e \n'
            'maior abrangência para a empresa.')


#===Caminho do seu arquivo local
caminho_arquivo = 'archives/Relatorio_Final.txt'

#===Ler o conteúdo do arquivo para passar ao botão
try:
    # Alterado encoding para latin-1 para aceitar a acentuação do arquivo
    with open(caminho_arquivo, "r", encoding="latin-1") as f:
        conteudo_arquivo = f.read()
except FileNotFoundError:
    conteudo_arquivo = "Arquivo de relatório não encontrado no servidor local."

#===Botão do download corrigido
st.download_button(
    label='Clieque aqui para baixar o relatório',
    data=conteudo_arquivo,              #===Conteúdo real do arquivo enviado aqui
    file_name='Relatorio_Final.txt',
    mime='text/plain'                   #===Tipo MIME correto para arquivos .txt
)

st.image('archives/logo_KMA.jpeg', width=1000)
