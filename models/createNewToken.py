from config.database import db
cursor = db.cursor()
def setnewToken(id,token):
    try:
        cursor.execute("UPDATE users SET token = %s WHERE id = %s",(token,id))
        db.commit()
    except:
        print("Error occured in createNewToken")