from flask import flash, redirect, render_template, url_for
from config.database import db
    
def valToken(token):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE token = '"+token+"'")
    result = cursor.fetchone()
    
    if not result:
       return flash("El token ya ha sido utilizado"),flash("Cierre la pestaña")
    else:
        idUser = result[0]
        query = "UPDATE users SET token = null, status = 'activo' WHERE id = %(id)s"
        cursor.execute(query, { 'id': idUser })
        db.commit()
        return redirect("/")

        