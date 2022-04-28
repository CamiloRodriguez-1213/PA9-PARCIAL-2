from config.database import db
cursor = db.cursor()
def setNewImage(description,name_product,user):
    try:
        cursor.execute("INSERT INTO images (name,route,user) VALUES (%s,%s,%s)",(description,name_product,user))
        db.commit()
        return True
    except:
        print("Error occured in createNewImage")
        return False