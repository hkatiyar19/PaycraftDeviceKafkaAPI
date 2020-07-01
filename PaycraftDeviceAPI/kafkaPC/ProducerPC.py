from kafka import KafkaProducer


class Producer:
    """Create a Producer class to send the post messages to Kafka broker."""
    message = '' #class attribute initialized

    def run(self):
        producer = KafkaProducer(bootstrap_servers='localhost:9092')
        topic = 'cpuUsage'

        producer.send(topic, bytes(Producer.message, "UTF-8")).get(timeout=10)

        producer.close()


def producer_run():
    """Run the Producer through Instance."""
    Producer().run()

