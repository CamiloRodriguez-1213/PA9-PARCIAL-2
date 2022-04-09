from flask import flash, redirect
from werkzeug.security import check_password_hash

from config.database import db
cursor = db.cursor()

def User(email,password):
    try:
        cursor.execute("SELECT * FROM users WHERE email = '"+email+"'")
        myresult = cursor.fetchone()
        checkPass = check_password_hash(myresult[3],password)
        return checkPass
    except:
        db.rollback()
        print("Error occured")
    
    
    
    