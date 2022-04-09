from config.database import db
from flask import flash, redirect,render_template
from werkzeug.security import generate_password_hash, check_password_hash
from models.welcomeEmail import sendMail
from models import validationToken
import re
import string
import random
cursor = db.cursor()

def createuser(nameUser,emailUser,passwordUser):
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
            cursor.execute("SELECT * FROM users WHERE email = '"+email+"'")
            myresult = cursor.fetchone()
            if myresult != None:
                flash("El email "+email+" ya se encuentra registrado")
                return redirect('/signup')
            else:
                passwordCod=generate_password_hash(password)
                userAuth = True
                length_of_string = 6
                token =(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)))
                emailReceived = sendMail(nameUser,emailUser,passwordCod,token)
                if emailReceived == True:
                    print("Correo enviado")
                    cursor.execute("INSERT INTO users (name,email,password,status,token) VALUES (%s,%s,%s,'inactivo',%s)",(name,email,passwordCod,token))
                    db.commit()
                    
                
        return userAuth
    except:
        db.rollback()
        print("Error occured")
      

    