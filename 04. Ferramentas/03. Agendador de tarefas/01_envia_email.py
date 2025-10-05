import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Dados do remetente
email_remetente = "joth10j@gmail.com"
senha = "20166925j"

# Dados do destinatário
email_destinatario = "joth10j@gmail.com"
assunto = "Assunto do Email"
corpo = "Olá! Este é um e-mail enviado via Python."

# Criar o e-mail
mensagem = MIMEMultipart()
mensagem['From'] = email_remetente
mensagem['To'] = email_destinatario
mensagem['Subject'] = assunto

# Adicionar o corpo do e-mail
mensagem.attach(MIMEText(corpo, 'plain'))

# Enviar o e-mail via servidor SMTP do Gmail
try:
    servidor = smtplib.SMTP('smtp.gmail.com', 587)
    servidor.starttls()  # Criptografa a conexão
    servidor.login(email_remetente, senha)
    servidor.send_message(mensagem)
    servidor.quit()
    print("E-mail enviado com sucesso!")
except Exception as e:
    print(f"Erro ao enviar e-mail: {e}")
