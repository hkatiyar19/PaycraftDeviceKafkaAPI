from PaycraftDeviceAPI.models.DeviceModel import Device
from flask_restful import Resource
from flask_jwt_extended import jwt_required


class DeviceAvgUsage(Resource):
    
    """To get the running average of CPU usages for a particular device, we maintain a txt file of cpu usages alongwith the timestamp,
       to calculate the average at runtime."""
       
    
    @jwt_required   #For authentication purpose
    def get(self,dev_id):
    
        device = Device.get_by_device_id(dev_id)
        if device :
            data = []
            with open(f'logs/{dev_id}.txt') as f: # Using the generated txt file while POST request to calculate average
                for line in f:
                    fields = line.rsplit(':')[-1]
                    x = int(fields[:2])
                    data.append(x)
            avg = sum(data) / len(data)
            return {'Device_ID':dev_id,'Average_CPU_Usage':avg},200
        else:
            return {'message':'No Device Found'},400