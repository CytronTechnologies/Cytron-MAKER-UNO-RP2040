"""
DESCRIPTION:
This example code uses Maker Uno RP2040 to control the onboard NeoPixel RGB LED.
In this code, the LEDs will cycle through colors in a loop, creating a color-changing effect.

The RGB LEDs is internally connected to GP25

AUTHOR  : Cytron Technologies Sdn Bhd
WEBSITE  : www.cytron.io
EMAIL    : support@cytron.io
"""
# Import necessary libraries
# Ensure that the "neopixel" library is uploaded to the board
from machine import Pin
import neopixel
import time

# Initialize NeoPixel with 2 LEDs on Pin 18
pixels = neopixel.NeoPixel(Pin(25), 2)
# Turn off all LEDs initially
pixels.fill((0, 0, 0))
# Set pixel brightness
pixels.brightness = 0.5

# Define each colour codes in RGB decimal format
RED = (255, 0, 0)
ORANGE = (255,180,0)
YELLOW = (80, 80, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (100, 100, 100)

# Create a list/array for the colours
colour = [RED,ORANGE,YELLOW,GREEN,CYAN,BLUE,PURPLE,WHITE]

# Cycle through each color in the list
while True:
    # Light up the neopixel RGB LED and change the colour every 0.15s
    for i in range(len(colour)):
        pixels.fill(colour[i])
        pixels.write()
        time.sleep(0.5)
