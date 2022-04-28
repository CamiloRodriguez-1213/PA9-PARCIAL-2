from colorama import Cursor
from config.database import db
cursor = db.cursor()
def change(id,status):
    
    try:
        if status == 'activo':
            estado= 'inactivo'
        if status == 'inactivo':
            estado= 'activo'
        cursor.execute("UPDATE images SET status = %s WHERE id = %s ",(estado,id))
        db.commit()
        return True
    except:
        print("Error occured in updateUSer")
        return False