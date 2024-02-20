"""
DESCRIPTION:
This example code will uses Maker Uno RP2040 with Ultrasonic Sensor HC-SR04P to read, measure and display distance in the REPL
to read distance from Ultrasonic Sensor HC-SR04P.

CONNECTION:
Grove 6 of Maker UNO RP2040 : HC-SR04P

GP20 - Echo
GP21 - Trig

AUTHOR   : Cytron Technologies Sdn Bhd
WEBSITE  : www.cytron.io
EMAIL    : support@cytron.io

"""
#Import necessary libraries
import time
import board
import digitalio
import adafruit_hcsr04

#Define pin GP20 and GP21 used on the board
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.GP20, echo_pin=board.GP21)

while True:
    
    Distance = sonar.distance
    print('Distance : ', Distance, 'cm')
    time.sleep(1)
