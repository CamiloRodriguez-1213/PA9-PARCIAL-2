from flask import flash, redirect
from models import getUser
from models import updateStatusUser
def valToken(token):
    result = getUser.getToken(token)
    if not result == None:
        idUser = result[0]
        if updateStatusUser.setnewToken(idUser):
            value = True
    else:
        value = False
        flash('El token ya ha sido utilizado','error'),flash('Cierre la pestaña','error')
    return value
def validate(id,token):
    user = getUser.userID(id,token)
    if user == None or user[4] == 'null':
        flash('La dirección url es incorrecta o ya se ha utilizado este token','error')
        return False
    else:
        return True
    
def validateToken(id):
    result = getUser.IdUser(id)
    
    if result[4] == 'null':
        print(result)
        flash('La dirección url es incorrecta o ya se ha utilizado este token','error')
        return False
    else:
        return True
    