from smtplib import SMTP 
from email.message import EmailMessage
from config import settings
from models import validationToken


def sendMail(name,email,password,token):
    try:
        message = EmailMessage()
        message ['Subject'] = "Hola "+name+", te damos la bienvenida a nuestra página"
        message['From'] = 'andresrodriguez2020@itp.edu.co'
        message['To'] = email
        message.set_content("<h2>Bienvenido a My-App "+name+" </h2>\n<h4>Activa tu cuenta dando clic al siguiente botón </h4>\n <a target='_blank' href='http://localhost:5000/authToken/"+token+"'><button>Activa tu cuenta</button></a>", subtype='html')
        username = settings.SMTP_USERNAME
        password = settings.SMTP_PASSWORD
        server = SMTP(settings.SMTP_HOSTNAME)
        server.starttls()
        server.login(username,password)
        server.send_message(message)
        server.quit()
        received = True
        return received
    except:
        print("Error occured")
        received = False
    return received