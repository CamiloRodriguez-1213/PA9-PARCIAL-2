from smtplib import SMTP 
from email.message import EmailMessage
from config import settings

def sendMail(asunto,email,content):
    try:
        message = EmailMessage()
        message ['Subject'] = asunto
        message['From'] = 'andresrodriguez2020@itp.edu.co'
        message['To'] = email
        message.set_content(content, subtype='html')
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
