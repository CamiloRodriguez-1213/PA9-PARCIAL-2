from config.database import db
from flask import flash, redirect,render_template
cursor = db.cursor()

def createuser(name,email,password):
    
    try:
        cursor.execute("SELECT * FROM users WHERE email = '"+email+"'")
        myresult = cursor.fetchone()
        if myresult != None:
            flash("Ya se encuentra registrado este usuario")
            return redirect('/signup')  
        else:
            flash ("Usuario registrado exitosamente")
            cursor.execute("INSERT INTO users (name,email,password) VALUES (%s,%s,%s)",(name,email,password))
        print("Query Excecuted successfully")
    except:
        db.rollback()
        print("Error occured")
    db.commit()
    