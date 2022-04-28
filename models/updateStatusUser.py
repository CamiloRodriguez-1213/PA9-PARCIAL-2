from colorama import Cursor
from config.database import db
cursor = db.cursor()
def setnewToken(id):
    estado= 'activo'
    try:
        cursor.execute("UPDATE users SET status = %s, token = NULL WHERE id = %s ",(estado,id))
        db.commit()
        return True
    except:
        print("Error occured in updateUSer")
        return False