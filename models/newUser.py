from config.database import db
from flask import redirect
cursor = db.cursor()

def createuser(name,email,password):
    cursor.execute("INSERT INTO users (name,email,password) VALUES (%s,%s,%s)",(name,email,password))
    db.commit()
    