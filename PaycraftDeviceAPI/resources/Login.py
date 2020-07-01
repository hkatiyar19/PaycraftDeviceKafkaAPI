from flask_jwt_extended import create_access_token
from PaycraftDeviceAPI.models.DeviceModel import Device
from werkzeug.security import safe_str_cmp
from flask_restful import Resource,reqparse

class Login(Resource):

    """Creating Login resource for authentication handling."""
    parser = reqparse.RequestParser()
    parser.add_argument('device_id', type=int, required=True)
    parser.add_argument('password', type=str, required=True)

    @classmethod
    def post(cls):
        data = cls.parser.parse_args()
        dev = Device.get_by_device_id(data['device_id'])

        if dev and safe_str_cmp(dev.password, data['password']):
            at = create_access_token(identity=dev.id,fresh=True)
            return {'access_token' : at},200
        return {'message':'This is wrong.'},401
