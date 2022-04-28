from config.database import db
cursor = db.cursor()
def getSign(email):
    try:
        cursor.execute("SELECT * FROM users WHERE email = '"+email+"'")
        myresult = cursor.fetchone()
        return myresult
    except:
        db.rollback()
        print("Error occured in getSign")