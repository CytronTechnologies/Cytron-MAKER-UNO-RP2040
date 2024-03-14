"""
DESCRIPTION:
This example code uses the Maker Uno RP2040 with the Ultrasonic Sensor HC-SR04P to read
and display the distance readings on an OLED display.

CONNECTION:

Maker Uno RP2040 Grove 6 with HC-SR04P
GP20 - Trig
GP21 - Echo

Maker UNO RP2040 Grove 5 with SSD1306 OLED Display
GP28 - SDA
GP29 - SCL


AUTHOR   : Cytron Technologies Sdn Bhd
WEBSITE  : www.cytron.io
EMAIL    : support@cytron.io

REFERENCE:
https://microcontrollerslab.com/hc-sr04-ultrasonic-sensor-raspberry-pi-pico-micropython-tutorial/ 

"""
# Import necessary libraries
# Ensure the "hcsr04" and "ssd1306" libraries are uploaded to the board
from machine import Pin, I2C
from hcsr04 import HCSR04
from time import sleep
from ssd1306 import SSD1306_I2C

# Define the connection of trigger and echo with the timeout settings
sonar = HCSR04(trigger_pin=20, echo_pin=21, echo_timeout_us=10000)

# Initialize the I2C method (channel number, SDA pin, SCL pin, Frequency)
i2c=I2C(0,sda=Pin(28), scl=Pin(29), freq=400000)
# Create an object 'oled' of SSD1306_I2C used with the width (128 pixels), height (64 pixels) and the i2c object as parameters.
oled = SSD1306_I2C(128, 64, i2c)

while True:
    # Clear the OLED screen
    oled fill(0)
    # Measure the distance in centimeters using the ultrasonic sensor
    distance = str(sonar.distance_cm())
    
    # Display readings on OLED
    oled.text("Distance", 0,15) # Display "Distance" text on the OLED screen 
    oled.text(distance +" cm", 0,35) 
    oled.show() # Update the OLED display
    
    sleep(1)
