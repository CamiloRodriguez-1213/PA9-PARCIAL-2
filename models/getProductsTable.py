from operator import imod
from config.database import db
from flask import jsonify,request

def getTable(insertar,fila,filaPagina,buscarValor,campoOrd,ordenDir):
    try:
        cursor=db.cursor()
        cursor.execute("SELECT count(*) AS allcount FROM products ")
        totalRegistro = cursor.fetchone()
        registrosTotales = totalRegistro[0]
        busqueda = "%" + buscarValor +"%"
        cursor.execute("SELECT count(*) AS allcount FROM products WHERE name_product LIKE %s OR description LIKE %s", (busqueda, busqueda))
        print(cursor)
        totalRegistro = cursor.fetchone()
        totalRegistroBusqueda = totalRegistro[0]
        if buscarValor=='':
            cursor.execute("SELECT * FROM products ORDER BY "+campoOrd+" "+ordenDir+" limit %s, %s", (fila, filaPagina))
            datos = cursor.fetchall()
        else:
            cursor.execute("SELECT * FROM products WHERE name_product LIKE %s OR description LIKE %s ORDER BY "+campoOrd+" "+ordenDir+" limit %s, %s;", (busqueda, busqueda, fila, filaPagina))
            datos = cursor.fetchall()
        print(datos)
        data = []
        for fila in datos:  
            data.append({
                'id': fila[0],
                'name_product': fila[1],
                'description': fila[2],
                'amount': fila[3],
                'price': fila[4],
            })
        response = {
                'draw': insertar,
                'iTotalRecords': registrosTotales,
                'iTotalDisplayRecords': totalRegistroBusqueda,
                'aaData': data,
            }
        return response
    except Exception as ex:
        print(ex)
    finally:
        cursor.close()