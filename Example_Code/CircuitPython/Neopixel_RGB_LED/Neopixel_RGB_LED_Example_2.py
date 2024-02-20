"""
DESCRIPTION:
This example code will uses Maker UNO RP2040 to control the onboard WS2812 RGB LEDs both individually and all together.
The first LED will blink in various colors, followed by the second LED, and eventually, both LEDs will light up together.

AUTHOR   : Cytron Technologies Sdn Bhd
WEBSITE  : www.cytron.io
EMAIL    : support@cytron.io

"""
# Import necessary libraries
import board
import neopixel
import time

# Initialize Neopixel RGB LED on pin GP25 and declare the number LEDs
pixel = neopixel.NeoPixel(board.GP25,2 )
# Clear Neopixel RGB LED
pixel.fill(0)
# Set pixel brightness
pixel.brightness = 0.5 #set brightness to 50%

# Define each colour codes in RGB decimal format
RED = (255, 0, 0)
ORANGE = (255,127,0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
INDIGO = (75, 0, 130)
PURPLE = (148, 0, 211)
WHITE = (100, 100, 100)

# Group all the colours for each LED in an array
colour1 = [RED,ORANGE,YELLOW,GREEN]
colour2 = [BLUE,INDIGO,PURPLE,WHITE]

# Create a combined list of colors for both LEDs
colour_both = colour1 + colour2

while True:
    
    # Blink the first LED with multiple colors from colour1 array
    for i in colour1:
        pixel[0] = i  # Turn on the first LED with the current color
        time.sleep(0.2)  # Keep the color for 0.2 seconds
        pixel[0] = (0, 0, 0)  # Turn off the first LED
        time.sleep(0.2)  # Wait for 0.2 seconds

    # Blink the second LED with multiple colors colour1 array
    for i in colour2:
        pixel[1] = i  # Turn on the second LED with the current color
        time.sleep(0.2)  # Keep the color for 0.2seconds
        pixel[1] = (0, 0, 0)  # Turn off the second LED
        time.sleep(0.2)  # Wait for 0.2 seconds

    # Turn on both LEDs with white color
    pixel.fill(WHITE)
    time.sleep(2)  # Keep both LEDs on for 2 seconds
    
    # Blink the all LEDs with multiple colors from the combined list of colour1 and colour2
    for i in range(len(colour_both)):
        pixel.fill((colour_both)[i])
        time.sleep(0.3)
    # Turn off all LEDs
    pixel.fill((0, 0, 0))
    time.sleep(0.2)

