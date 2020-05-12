from kafka import KafkaConsumer
import time
import infrastructure.DataBase as database
from datetime import datetime

def consumeRecords(topicName,bootstrap_servers,mariadb_connection,cursor):
    productos = []
    while(True):

        consumer = KafkaConsumer(topicName, group_id = 'group1',bootstrap_servers = bootstrap_servers,
                                 auto_offset_reset = 'earliest')
        for message in consumer:
            evento = bytes.decode(message.value)
            print(evento)
            productos.append(evento)
            producto = evento.split(":")[0]
            idProducto = evento.split(":")[1]
            eventoCreado = datetime.fromtimestamp(float(message.timestamp)/1000).strftime('%Y-%m-%d %H:%M:%S.%f')
            eventoRecibido= datetime.now()
            database.insertProducts(cursor,producto,idProducto,eventoCreado,eventoRecibido)
            mariadb_connection.commit()

def main():
    time.sleep(5)
    mariadb_connection,cursor = database.connectDatabase()

    bootstrap_servers = ['kafka:9092']
    #localhost
    #bootstrap_servers = ['localhost:29092']

    topicName = 'test_1'
    database.printProducts(cursor)

    consumeRecords(topicName,bootstrap_servers,mariadb_connection,cursor)


if __name__== "__main__":
    main()