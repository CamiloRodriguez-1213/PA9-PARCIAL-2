from config.database import db

cursor = db.cursor()
def setNewPassword(password,id):
    try:
        cursor.execute("UPDATE users SET password = %s, token = null  WHERE id = %s",(password,id))
        db.commit()
        
        return True
    except:
        return False
    