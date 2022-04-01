from config.database import db
cursor = db.cursor()
def obtenerProductos():
    sql = "SELECT * FROM users"
    cursor.execute(sql)
    results= cursor.fetchall()
    return results
def crearProducto(name,email,password):
    cursor.execute("INSERT INTO users (name,email,password) VALUES (%s,%s,%s)",(name,email,password))
    db.commit()