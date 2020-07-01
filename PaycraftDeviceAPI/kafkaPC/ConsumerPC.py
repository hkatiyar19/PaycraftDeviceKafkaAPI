from PaycraftDeviceAPI.consume_to_db import SaveDevice
from kafka import KafkaConsumer

class Consumer:
    """create a consumer class to get messages from Kafka broker and operate on data"""
    
    def run(self):
        
        topic = 'cpuUsage'
        consumer = KafkaConsumer(topic, bootstrap_servers='localhost:9092', group_id='device') #creating Consumer obect
       
        for message in consumer:
            data = (message.value).decode('utf-8').split(',')
            """Get the message from Consumer record over iteration and save to database"""
            SaveDevice.dev_to_db(data)


if __name__ == '__main__':
    """ Run consumer through instance"""
    Consumer().run()