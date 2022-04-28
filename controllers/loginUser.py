
from flask import flash,render_template,redirect,session
from werkzeug.security import check_password_hash,generate_password_hash
import re
from models.getGenerateToken import newToken
from models.createSendingEmail import sendMail
from models.createActiveUser import setUserInactive
from models import getEmailExist
def signin(email,password):
    try:
        if email is '':
            flash('Correo electrónico','error')
        if password is '':
            flash('Contraseña','error')
        else:
            if not getEmailExist.getSign(email) == None:
                result = getEmailExist.getSign(email)
                checkPass = check_password_hash(result[3],password)
                if checkPass:
                    if result[4] == 'activo':
                        session['token'] = result[0]
                        session['user'] = result[1]
                        session['username'] = result[2]
                        return checkPass
                    else:
                        return flash("La cuenta aún no ha sido activada, revisa tu correo electrónico",'error')
                else:
                    flash('Usuario o contraseña incorrectos','error')
            else:
                flash("El usuario no existe",'error')
        return checkPass
    except:
        print("Error occured in signinUser")
                
def signUp(nameUser,emailUser,passwordUser):
    try:
        name = nameUser
        email = emailUser
        password = passwordUser
        isValid = True
        patternpw=re.compile('(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,20}')
        passwordval = re.search(patternpw, password)
        
        userAuth = False
        if name == '':
            isValid = False
            flash('* Nombre')
        if email == '':
            isValid = False
            flash('* Email')
        if not passwordval or password=='':
            isValid = False
            flash('* Contraseña:')
            flash('El campo contraseña debe contener un mínimo de 8 caracteres, un máximo de 20, letras, (minúsculas y MAYÚSCULAS) y Números')
        if isValid == False:
            return render_template("/views/login/signup.html", name = name, email = email)
        else:
            result = getEmailExist.getSign(email)
            if result:
                flash("El email "+email+" ya se encuentra registrado")
                return redirect('/signup')
            else:
                passwordCod=generate_password_hash(password)
                token = newToken()
                
                asunto = "Hola "+name+", te damos la bienvenida a nuestra página"
                content = "<h2>Bienvenido a My-App "+name+" </h2>\n<h4>Activa tu cuenta dando clic al siguiente botón </h4>\n<a target='_blank' href='http://localhost:5000/authToken/"+token+"'><button>Activa tu cuenta</button></a>"
                emailReceived = sendMail(asunto,email,content)
                emailReceived = True
                if emailReceived == True:
                    print("Correo enviado")
                    setUserInactive(name,email,passwordCod,token)
                    userAuth = True
        print (userAuth)
        return userAuth
    except:
        print("Error occured")
        flash("Ha habido un problema al enviar el correo")
      

    