import pymysql

def conectar_db():
    return pymysql.connect(
        host="localhost",
        user="nommail_user",
        password="1234",
        database="nom_mail",
        cursorclass=pymysql.cursors.Cursor
    )

def insertar_usuario(nombre, mail):
    db = conectar_db()
    cursor = db.cursor()
    sql = "INSERT INTO usuarios (Nombre, Mail) VALUES (%s, %s)"
    cursor.execute(sql, (nombre, mail))
    db.commit()
    cursor.close()
    db.close()

def obtener_mail(nombre):
    db = conectar_db()
    cursor = db.cursor()
    sql = "SELECT Mail FROM usuarios WHERE Nombre = %s"
    cursor.execute(sql, (nombre,))
    resultado = cursor.fetchone()
    cursor.close()
    db.close()
    return resultado
