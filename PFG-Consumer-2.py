from kafka import KafkaConsumer


def main():
    while(True):
        bootstrap_servers = ['localhost:9092']
        topicName = 'test_1'
        consumer = KafkaConsumer(topicName, group_id = 'group1',bootstrap_servers = bootstrap_servers,
                          auto_offset_reset = 'earliest')
        for message in consumer:
            message = message.value
            print(message)

if __name__== "__main__":
    main()