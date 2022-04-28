from flask import flash
from werkzeug.security import generate_password_hash
import re
from models import createNewPassword
def changePassword(id,password):
    try:
        patternpw=re.compile('(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,20}')
        passwordval = re.search(patternpw, password)
        userAuth = False
        if not passwordval or password=='':
            flash('* Contraseña:')
            flash('El campo contraseña debe contener un mínimo de 8 caracteres, un máximo de 20, letras, (minúsculas y MAYÚSCULAS) y Números')
        else:
            passwordCod=generate_password_hash(password)
            createNewPassword.setNewPassword(passwordCod,id)
            userAuth = True
            flash('Se ha realizado el cambio de contraseña exitosamente','good')
        return userAuth
    except:
        print("Error occured")
        flash("Ha habido un problema al cambiar la contraseña",'error')
        flash("Vuelva a intentarlo",'error')