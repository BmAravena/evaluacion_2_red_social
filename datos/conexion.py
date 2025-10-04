import mysql.connector


try:
    db  = mysql.connector.connect()
    host="localhost",        # O la IP/host de tu servidor MySQL
    user="root",       # usuario de la BD
    password="",    # contraseña del usuario
    database="red_social"   # nombre de la base de datos
    mycursor = db.cursor()

except Exception as e:
    print(f"Error {e}")
