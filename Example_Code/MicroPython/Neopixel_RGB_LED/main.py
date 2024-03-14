"""
DESCRIPTION:
This example code show how to use the two onboard RGB LEDs of the Maker Uno RP2040.
It highlight the basic control of the  RGB LEDs.
This include turning each LED or all LEDs to specific colors.

The RGB LEDs in internally connected to GP25


AUTHOR   : Cytron Technologies Sdn Bhd
WEBSITE  : www.cytron.io
EMAIL    : support@cytron.io

"""
# Import necessary libraries
from machine import Pin
import neopixel
import time

# Initialize NeoPixel object with 2 LEDs on Pin 25
pixels = neopixel.NeoPixel(Pin(18), 2)

# Turn off both LEDs initially
pixels[0] = (0, 0, 0)
pixels[1] = (0, 0, 0)
pixels.write()
# Set brightness to 50%
pixels.brightness = 0.5

while True:
    
    # Turn on each LED individually to the desired color simultaneously
    # The sequence of the colour code is (R,G,B) with an input range from 0-255 (decimal)
    pixels[0] = (200, 0, 0) #Red
    pixels[1] = (0, 0, 200) #Blue
    pixels.write()
    time.sleep(1)
    
    # Turn off both LEDs
    pixels[0] = (0, 0, 0)
    pixels[1] = (0, 0, 0)
    pixels.write()
    time.sleep(1)
    
    # Turn all LEDs to a specified colour
    pixels.fill((0,200,0)) #Green
    time.sleep(1)
    
    # Turn off both LEDs
    pixels[0] = (0, 0, 0)
    pixels[1] = (0, 0, 0)
    pixels.write()
    time.sleep(1)
    
    
