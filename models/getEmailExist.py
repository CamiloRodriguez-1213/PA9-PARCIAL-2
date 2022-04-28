from config.database import db
cursor = db.cursor()
def getSign(email):
    try:
        cursor.execute("SELECT * FROM users WHERE email = '"+email+"'")
        myresult = cursor.fetchone()
        return myresult
    except:
        
        
        print("Error occured in getEmailExist")