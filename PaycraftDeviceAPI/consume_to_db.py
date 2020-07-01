from PaycraftDeviceAPI.models.DeviceModel import Device
from PaycraftDeviceAPI.consumerApp import consumer_app


class SaveDevice:
    """Creating class for saving the operated data to database at Consumer end."""
    def dev_to_db(arr:list):
        with consumer_app.app_context() : # within Consumer application context,We'll be processing.
            try:
                if Device.get_by_device_id(int(arr[0])) is None :
                    dev = Device(int(arr[0]), arr[1], int(arr[2]))
                    dev.save_to_db()
            except Exception as e:
                print('Erroneous Data')












