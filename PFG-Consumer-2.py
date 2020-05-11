from kafka import KafkaConsumer
import mysql.connector as mariadb
import time
from datetime import datetime
def connectDatabase():
    #mariadb_connection = mariadb.connect(user='root', password='root',host='MariaDB', database='PFG-DATABASE')
    mariadb_connection = mariadb.connect(user='root', password='root', database='PFG-DATABASE')
    cursor = mariadb_connection.cursor()

    return mariadb_connection,cursor

def printProducts(cursor):
    print("Mostrando los productos de la base de datos")
    cursor.execute("SELECT Productos FROM Eventos ")
    for Productos in cursor:
        print(Productos)



def main():
    time.sleep(5)
    mariadb_connection,cursor = connectDatabase()
    productos = []
    bootstrap_servers = ['kafka:9092']
    #localhost
    #bootstrap_servers = ['localhost:29092']
    topicName = 'test_1'
    printProducts(cursor)
    while(True):

        consumer = KafkaConsumer(topicName, group_id = 'group1',bootstrap_servers = bootstrap_servers,
                          auto_offset_reset = 'earliest')
        for message in consumer:
            evento = bytes.decode(message.value)

            productos.append(evento)
            producto = evento.split(":")[0]
            idProducto = evento.split(":")[1]
            eventoCreado = datetime.fromtimestamp(float(message.timestamp)/1000).strftime('%Y-%m-%d %H:%M:%S.%f')
            eventoRecibido= datetime.now()
            query =("INSERT INTO Eventos (Productos,id,Creado,Recibido) VALUES (%s,%s,%s,%s)")
            cursor.execute(query,(producto,idProducto,eventoCreado,eventoRecibido,))
            mariadb_connection.commit()
            print(evento)

if __name__== "__main__":

    main()