import mysql.connector as mariadb

def connectDatabase():
    mariadb_connection = mariadb.connect(user='root', password='root',host='MariaDB', database='PFG-DATABASE')
    #mariadb_connection = mariadb.connect(user='root', password='root', database='PFG-DATABASE')
    cursor = mariadb_connection.cursor()

    return mariadb_connection,cursor

def printProducts(cursor):
    print("Mostrando los productos de la base de datos")
    cursor.execute("SELECT Productos FROM Eventos ")
    for Productos in cursor:
        print(Productos)

def insertProducts(cursor,producto,idProducto,eventoCreado,eventoRecibido):
    query =("INSERT INTO Eventos (Productos,id,Creado,Recibido) VALUES (%s,%s,%s,%s)")
    cursor.execute(query,(producto,idProducto,eventoCreado,eventoRecibido,))
