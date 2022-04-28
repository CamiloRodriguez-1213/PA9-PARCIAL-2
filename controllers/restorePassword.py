from flask import flash, redirect
from models.createSendingEmail import sendMail
from models.getUser import User
from models import createNewToken
from models.getGenerateToken import newToken
def restpass(email):
    user = []
    user = User(email)
    if not user ==None:
        id = str(user[0])
        token = newToken()
        createNewToken.setnewToken(id,token)
        messages = "Restablecimiento de contraseña"
        content = "<h2>Hola!</h2>\n<p>¿Has olvidado tu contraseña?\nNo te preocupes, vamos a reestablecer una nueva. \nPor favor haz clic en el siguiente enlace para activar una contraseña nueva:</p>\n<a target='_blank' href='http://localhost:5000/newPassword/"+id+"/"+token+"'><button>Restablecer contraseña</button></a>"
        emailReceived = sendMail(messages,email,content)
        if emailReceived:
            flash('Se ha enviado al correo electrónico los pasos para restablecer la contraseña','good')
            flash('Puede cerrar esta página','good')
        else:
            flash('No se ha podido enviar a su correo electrónico los pasos para restablecer la contraseña','error')
        return emailReceived