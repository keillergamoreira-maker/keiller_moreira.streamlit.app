#===Importar o Streamlit
import streamlit as st

#===Importar os módulos do e-mail
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


def enviar_email(remetente, senha, destinatario, assunto,
                 corpo, buffer_imagem, nome_arquivo):
    """Função responsável por enviar o e-mail"""
    #===Conectar com o Gmail
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    #===Informações dp e-mail
    mensagem = MIMEMultipart('mixed')
    mensagem['From'] = remetente
    mensagem['To'] = destinatario
    mensagem['Subject'] = assunto
    mensagem.attach(MIMEText(corpo,'plain'))

    #===Porcessar a imagem
    try:
        dados_imagem = buffer_imagem.getvalue()
        anexo = MIMEImage(dados_imagem)
        anexo.add_header('Content-Disposition', 'attachment', filename=nome_arquivo)
        mensagem.attach(anexo)
    except Exception as e:
        st.error(f'Erro ao processar a imagem da memória: {e}')
        return False

    #===Enviar o e-mail
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(remetente, senha)
        server.send_message(mensagem)
        server.quit()
    except Exception as e:
        st.error(f'Erro ao enviar o e-mail: {e}')
        return False

