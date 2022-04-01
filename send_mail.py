from smtplib import SMTP
from email.message import EmailMessage
from config import settings
message = EmailMessage()

message ['Subject'] = 'Este es el asunto'
message['From'] = 'andresrodriguez2020@itp.edu.co'
message['To'] = 'andrescamilocr482@gmail.com'
message.set_content('Este es un email de pruebas')

username = settings.SMTP_USERNAME
password = settings.SMTP_PASSWORD

server = SMTP(settings.SMTP_HOSTNAME)
server.starttls()
server.login(username,password)
server.send_message(message)
print(username,password)
server.quit()