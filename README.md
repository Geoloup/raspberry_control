# **Raspberry Pi controller**
## help
 [Raspberrypi controller Wiki](https://github.com/Geoloup/raspberry_control/wiki/)
## Feature
 1. Connect in ssh to the Raspberry Pi
 2.  Module and Global call are supported
 3. The function can be run on the Raspberry Pi  by adding `@raspberry_control.raspberry_command()` on top of a function and get the result
 4. Get Output of a function that was run on the raspberry
 5. Real-time output
 6. Run command on the Raspberry Pi with `raspberry_control.run_command("command here")`
 7. You can do `@raspberrypi.timeout(time,default)` will change the timeout for a functions
 8. Get file from the server and read it ? / write it localy and update after on the server
## Not supported
 1. .local adress
## Example

    import raspberrypi_control # import package for raspberrypi controlling over ssh  
    import os # raspberryPi control can automacly install package.
    import time  
      
    rp = raspberrypi_control # rp is for RaspberryPi  
      
    i = 1234567890  
      
      
    @rp.raspberry_command() # When function is called its automatcly run on the raspberrypi fallback : local
    def test():  
        print("Hello RaspBerryPi")  
        return "finished"  
      
      
    @rp.raspberry_command() # When function is called its automatcly run on the raspberrypi fallback : local
    def other():  
        global i  
        print("Hello RaspberryPi h")  
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
        rp.raspberrypi().set_raspberry_info("username here", "password here") # set login info here
        rp.raspberrypi().set_preparation("raspberrypi.local", 8, 1) # config locator for the raspberrypi  
        rp.raspberrypi().local() # set the start ip set in the line in the top  
        rp.config("main") # file name if this file (no .py)  
        rp.run_command("Hello World",True) # true is for if console ouput is print or no
        print(test())  
        print(other()) # you can get the output after

## How to install the package
Do `pip install raspberry-control`
Supported for python 3.10 and higher*
*note not tested for lower version

## Bug report
[Github - Issues](https://github.com/Geoloup/raspberry_control/issues/new?assignees=franck403&labels=bug&projects=&template=bug-report.yml&title=%5BBUG%5D+Untitled+Bug+Report)
