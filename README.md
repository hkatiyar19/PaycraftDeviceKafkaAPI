# PaycraftDeviceKafkaAPI
This is a simulation of the Rest API at the Client end sending data to the Apache Kafka broker and get it consumed, operated and saved to database.

For Kafka broker Simulation :

1.We start Client side application( PCapp ) first.
2.As the data is posted through api endpoint, producer (ProducerPC) is invoked with data (DeviceRegister Resource) and sends it further to the Kafka broker.
3.As testing in stand-alone system, we stop the client side application( PCapp ) and start the server-side application ( consumer_app ).
4.As soon as server-side/Consumer application starts, We invoke/start the consumer ( ConsumerPC ) to consume messages from Kafka broker at the latest offset.
5.Consumer gets the message and further sends the data to be operated and saved to database.(consume_to_db)

For getting the running average of CPU Usage:

We can achieve this through Kafka incremental functions of sum and count, though Kafka doesn't offer incremental average so it'll not be possible to get the average directly but
only through sum/count method which is represented in DeviceUsage Resource at the client end.
