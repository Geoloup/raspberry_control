import raspberrypi_control  # import package for raspberrypi controlling over ssh
import os  # Put import here they are take and install to the raspberrypi file.
import time

rp = raspberrypi_control  # rp is for RaspBerryPi

i = 1234567890


@rp.raspberry_command()  # run code and you're raspberrypi. If the raspberrypi was not find it's will be run in local.
def test():
    print("Hello RaspBerryPi")
    return "finished"


@rp.raspberry_command()  # run code and you're raspberrypi. If the raspberrypi was not find it's will be run in local
def other():
    global i
    print("Hello RaspBerryPi h")
    th = 0
    print(i)
    os.system("echo Hello World")
    while True:
        th = th + 1
        if th == 30:
            time.sleep(0.1)
            break
    return th

if __name__ == "__main__":  # put all you're code to run at start here. Because if not the code will be run 2 time
    rp.raspberrypi().set_raspberry_info("username here", "password here") # set login info here
    rp.raspberrypi().set_preparation("adress/ip here", 8, 1)  # config locator for the raspberrypi
    rp.raspberrypi().local()  # set the start ip set in the line in the top
    rp.config("main")  # file name (no .py)
    print(test())
    print(other())  # you can get the output after
