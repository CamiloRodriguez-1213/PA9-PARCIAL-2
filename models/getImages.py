from config.database import db
cursor = db.cursor()
def getImagesUser(token):
    try:
        token = str(token)
        cursor.execute("SELECT * FROM images,users WHERE images.user = '"+token+"' ")
        myresult = cursor.fetchall()
        return myresult
    except: 
        print("Error occured in getImagen")
def getImages():
    try:
        cursor.execute("SELECT * FROM images,users WHERE images.status= 'activo'")
        myresult = cursor.fetchall()
        return myresult
    except: 
        print("Error occured in getImagen")
def getImagesId(id):
    try:
        cursor.execute("SELECT * FROM images,users WHERE images.id = '"+id+"' ")
        myresult = cursor.fetchone()
        return myresult
    except: 
        print("Error occured in getImagenId")