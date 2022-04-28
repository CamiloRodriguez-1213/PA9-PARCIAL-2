from config.database import db
from flask import flash
cursor = db.cursor()
def User(email):
    try:
        cursor.execute("SELECT * FROM users WHERE email = '"+email+"'")
        myresult = cursor.fetchone()
        id = myresult[0]
        name = myresult[1]
        email = myresult[2]
        status = myresult[4]
        
        user = [id,name,email,status]
        
        return user
    except: 
        print("Error occured in getUser")
        return flash('El email '+email+' no está registrado','error')
    
def userID(id,token):
    try:
        id= int(id)
        if id>0:
            cursor.execute("SELECT * FROM users WHERE id = %s and token = %s",(id,token))
            myresult = cursor.fetchone()
            id = myresult[0]
            name = myresult[1]
            email = myresult[2]
            status = myresult[4]
            token = myresult[5]
            
            user = [id,name,email,status,token]
        return user
    except: 
        print("Error occured in getUser")
def IdUser(id):
    try:
        cursor.execute("SELECT * FROM users WHERE id = '"+id+"'")
        myresult = cursor.fetchone()
        id = myresult[0]
        name = myresult[1]
        email = myresult[2]
        status = myresult[4]
        token = myresult[5]
        
        userId = [id,name,email,status,token]
        return userId
    except: 
        print("Error occured in getIDUser")
def getToken(token):
    try:
        cursor.execute("SELECT * FROM users WHERE token = '"+token+"'")
        myresult = cursor.fetchone()
        return myresult
    except: 
        print("Error occured in getToken")
