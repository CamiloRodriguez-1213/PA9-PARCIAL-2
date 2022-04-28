
from config.database import db
cursor = db.cursor()
def deleteImage(id):
    try:
        cursor.execute("DELETE FROM images where id = '"+id+"'")
        db.commit()
        return True
    except:
        return False