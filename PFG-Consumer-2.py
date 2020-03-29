from kafka import KafkaConsumer
import mysql.connector as mariadb
import schedule

def connectDatabase():
    mariadb_connection = mariadb.connect(user='root', password='root', database='PFG-DATABASE')
    cursor = mariadb_connection.cursor()

    return mariadb_connection,cursor

def printProducts():
    print("Mostrando los productos de la base de datos")
    cursor.execute("SELECT Productos FROM Eventos ")
    for Productos in cursor:
        print(Productos)

def main(mariadb_connection,cursor):

    bootstrap_servers = ['localhost:9092']
    topicName = 'test_1'
    while(True):
        #schedule.every(2).seconds.do(printProducts())
        consumer = KafkaConsumer(topicName, group_id = 'group1',bootstrap_servers = bootstrap_servers,
                          auto_offset_reset = 'earliest')
        for message in consumer:
            evento = bytes.decode(message.value)
            query =("INSERT INTO Eventos (Productos) VALUES (%s)")
            cursor.execute(query,(evento,))
            mariadb_connection.commit()
            print(evento)
            print(message)

if __name__== "__main__":

    mariadb_connection,cursor = connectDatabase()

    main(mariadb_connection,cursor)