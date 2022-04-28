from config.database import db
cursor = db.cursor()
def setNewImage(description,name_product,user,id):
    print(description,name_product,user,id)
    try:
        cursor.execute("UPDATE images SET name = %s, route = %s, user = %s WHERE id = %s ",(description,name_product,user,id))
        db.commit()
        return True
    except:
        print("Error occured in createNewImage")
        return False