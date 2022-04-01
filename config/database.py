import mysql.connector as mysql
from . import settings

db = mysql.connect(
    host=settings.MYSQL_HOSTNAME,
    user= settings.MYSQL_USERNAME,
    password=settings.MYSQL_PASSWORD,
    database=settings.MYSQL_DATABASE,
    port=settings.MYSQL_PORT
)
