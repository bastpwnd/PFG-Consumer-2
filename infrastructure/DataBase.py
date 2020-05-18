import mysql.connector as mariadb

#Method to connect MariaDB database
def connectDatabase():
    mariadb_connection = mariadb.connect(user='root', password='root',host='MariaDB', database='PFG-DATABASE')
    #mariadb_connection = mariadb.connect(user='root', password='root', database='PFG-DATABASE')
    cursor = mariadb_connection.cursor()

    return mariadb_connection,cursor

#Method to prints all products
def printProducts(cursor):
    print("Mostrando los productos de la base de datos")
    cursor.execute("SELECT Productos FROM Eventos ")
    for Productos in cursor:
        print(Productos)

#Method to insert events in database
def insertProducts(cursor,producto,idProducto,eventoCreado,eventoRecibido):
    query =("INSERT INTO Eventos (Productos,id,Creado,Recibido) VALUES (%s,%s,%s,%s)")
    cursor.execute(query,(producto,idProducto,eventoCreado,eventoRecibido,))
