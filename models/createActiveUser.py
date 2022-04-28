from config.database import db
cursor = db.cursor()
def setUserInactive(name,email,passwordCod,token):
    try:
        cursor.execute("INSERT INTO users (name,email,password,status,token) VALUES (%s,%s,%s,'inactivo',%s)",(name,email,passwordCod,token))
        db.commit()
    except:
        print("Error occured in createActiveUser")