"""
DESCRIPTION:
This example code will uses Maker Uno RP2040 to control the onboard LEDs.
Two LEDs (GP1 and GP0) will be blinking for each 0.5 second alternately.


AUTHOR   : Cytron Technologies Sdn Bhd
WEBSITE  : www.cytron.io
EMAIL    : support@cytron.io
"""
# Import the required module
from machine import Pin
import time

# Initialize leds on GP0 and GP1 pins as output
led1 = Pin(0, Pin.OUT)
led2 = Pin(1, Pin.OUT)

while True:
    # led1 light up for 0.5s then turned off
    led1.value(True)
    time.sleep(0.5)
    led1.value(False)
    time.sleep(0.5)

    # led2 light up for 0.5s then turned off
    led2.value(True)
    time.sleep(0.5)
    led2.value(False)
    time.sleep(0.5)

