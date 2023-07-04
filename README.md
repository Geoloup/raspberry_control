# **Raspberry Pi controller**
## Feature

 1. Connect in ssh to the Raspberry Pi
 2.  Module and Global call are supported
 3. The function can be run on the Raspberry Pi  by calling `@raspberry.raspberry_command()` and get the result
 4. Get Output of a function that was run on the raspberry
 5. Real-time output
 6. Run command on the Raspberry Pi with `raspberry.fun_command("command here")`
 7. You can do `@raspberrypi.timeout(time,default)` that will make the function stop after the time specified and stop if it's not finish
## Example

    import raspberrypi # import package for raspberrypi controlling over ssh  
    import os # Put import here they are take and install to the raspberrypi file.  
    import time  
      
    rp = raspberrypi # rp is for RaspBerryPi  
      
    i = 1234567890  
      
      
    @rp.raspberry_command() # run code and you're raspberrypi. If the raspberrypi was not find it's will be run in local.  
    def test():  
    print("Hello RaspBerryPi")  
    return "finished"  
      
      
    @rp.raspberry_command() # run code and you're raspberrypi. If the raspberrypi was not find it's will be run in local  
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
      
      
    if __name__ == "__main__": # put all you're code to run at start here. Because if not the code will be run 2 time  
    rp.raspberrypi().set_preparation("192.168.0.10", 8, 1) # config locator for the raspberrypi  
    rp.raspberrypi().local("192.168.0.10") # set the start ip set in the line in the top  
    rp.config("main") # file name if this file (no .py)  
    print(test())  
    print(other()) # you can get the output after

## How to install the package
Do `Pip install raspberry-control`
Supported for python 3.10 and higher*
*note not tested for lower version
