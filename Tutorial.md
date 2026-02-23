## A tutorial detailing the configuration of OpenCR as a communication and control interface between a computer and Dynamixel motors.
- Install requirements:  
Arduino : https://www.arduino.cc/en/software  
Python : https://www.python.org  
Dynamixel Wizard : https://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_wizard2  
Visual Studio Code : 
https://code.visualstudio.com

- Install and set up Arduino as this website : https://emanual.robotis.com/docs/en/parts/controller/opencr10  
- After set up Arduino, connect OpenCR board then go to File -> Examples -> OpenCR -> 10.Etc -> usb_to_dxl -> Upload.
- Open Dynamixel Wizard 2 -> Scan (Need to remember the baudrate, protocol, and ID of Motors) then click into each motor and explore its features -> Find ID in the control table to configure clearly for later to control grouped motors.
- When finished playing with the motors, unplug all motors except the PROTOCOL 1 MOTORS to update it. *Note: Have to update each motor at a time.
- Update motor step:
    - Tools -> Firmware recovery -> Next -> Select model of the motor to update then follow the instructions of the app.
- After install VSC (Visual Studio Code) go to Extensions or Ctrl + Shift + X then find and install Python and Python Debugger......