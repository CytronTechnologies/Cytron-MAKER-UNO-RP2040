"""
DESCRIPTION:
This example code uses the Maker Uno RP2040 with the Ultrasonic Sensor HC-SR04P
to read and display the distance in the Thonny IDE's shell console.

CONNECTION:
Maker Uno RP2040 Grove 6 with HC-SR04P
GP20 - Trig
GP21 - Echo

AUTHOR   : Cytron Technologies Sdn Bhd
WEBSITE  : www.cytron.io
EMAIL    : support@cytron.io

"""
# Import necessary libraries
# Ensure the "hcsr04" and "ssd1306" libraries are uploaded to the board
import time
from hcsr04 import HCSR04

# Define the connection of trigger and echo with the timeout settings
sonar = HCSR04(trigger_pin=20, echo_pin=21, echo_timeout_us=10000)

while True:
    # Measure the distance in centimeters using the ultrasonic sensor
    Distance = sonar.distance_cm()
    
    # Print the measured distance in centimeters
    print('Distance : ', Distance, 'cm')
    time.sleep(1)
