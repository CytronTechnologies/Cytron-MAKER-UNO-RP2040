"""
DESCRIPTION:
This example code will uses Maker Uno RP2040 to control the onboard LEDs.
The LEDs will light in sequence (one by one) and then turn off.

AUTHOR   : Cytron Technologies Sdn Bhd
WEBSITE  : www.cytron.io
EMAIL    : support@cytron.io

"""

# Import the required module
from machine import Pin
import time

# Define the pin numbers for the onboard LEDs
led_pins = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# Create a list of Pin objects for each LED using list comprehension method
# The list comprehension iterates over each pin in led_pins, creating a Pin object for each
leds = [Pin(pin, Pin.OUT) for pin in led_pins]

while True:
    
    # Turn on each LED in sequence with a short delay
    for i in range(len(led_pins)):
        leds[i].value(True)
        time.sleep(0.15)
    
    # Turn off each LED in sequence with a short delay
    for i in range(len(led_pins)):
        leds[i].value(False)
        time.sleep(0.15)
    
    # Turn on all LEDs together
    for led in leds:
        led.value(True)
    time.sleep(1)   
    
    # Turn off all LEDs together
    for led in leds:
        led.value(False)
    time.sleep(1)
        

