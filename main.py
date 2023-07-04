import raspberrypi_control  # import package for raspberrypi controlling over ssh
import os  # Put import here they are take and install to the raspberrypi file.
import time

rp = raspberrypi  # rp is for RaspBerryPi

i = 1234567890


@rp.raspberry_command()
def get_info():
    import socket
    import requests
    value = list()
    value.append(socket.gethostname())
    value.append(socket.AF_BLUETOOTH.value)
    val = requests.get("http://ip-api.com/json/").json()
    latitude = val["lat"]
    longitude = val["lon"]
    val = requests.get(f"https://geocode.maps.co/reverse?lat={latitude}&lon={longitude}").json()
    val.pop("licence")
    val.pop("powered_by")
    value.append(val["display_name"])
    return value


if __name__ == "__main__":  # put all you're code to run at start here. Because if not the code will be run 2 time
    rp.raspberrypi().set_preparation("192.168.0.10", 8, 1)  # config locator for the raspberrypi
    rp.raspberrypi().local("192.168.0.10")  # set the start ip set in the line in the top
    rp.config("main")  # file name if this file (no .py)
    print(get_info())
