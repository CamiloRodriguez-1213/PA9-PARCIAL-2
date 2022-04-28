from config.database import db
cursor = db.cursor()
def getTokenUSer(token):
    try:
        cursor.execute("SELECT * FROM users WHERE token = '"+token+"'")
        myresult = cursor.fetchone()
        
    except:
        db.rollback()
        print("Error occured in createActiveUser")