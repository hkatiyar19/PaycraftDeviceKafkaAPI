from flask_restful import Resource,reqparse
from PaycraftDeviceAPI.kafkaPC.ProducerPC import producer_run,Producer
import threading

class DeviceRegister(Resource):
    """Add args details to be parsed"""
    parser = reqparse.RequestParser()
    parser.add_argument('device_id', type=int, required=True)
    parser.add_argument('password', type=str, required=True)
    parser.add_argument('cpu_usage', type=int)
    parser.add_argument('timestamp',required=True)

    """Recieving Post data and sending to Kafka broker through Producer."""
    def post(self):
        data = DeviceRegister.parser.parse_args()
        try:
            Producer.message = str(data['device_id'])+','+data['password']+','+str(data['cpu_usage']) # Creating a String of the parsed arguments
            
            """Starting a Daemon thread for producer to automatically get killed after processing."""
            threading.Thread(target=producer_run,daemon=True).start()
            return {'message':'Data sent successfully.'},200
            
        except Exception as e:
            return {'message':'Invalid Data'},400
            
        finally:
            with open(f'logs/{data["device_id"]}.txt', 'a+') as f:  # create CPU usage file for average calculation.
                f.write(f'timestamp :{data["timestamp"]}, cpu_usage :{data["cpu_usage"]}\n')

      
