"""
DESCRIPTION:
This example code will uses Maker UNO RP2040 to control the onboard WS2812 RGB LEDs

AUTHOR   : Cytron Technologies Sdn Bhd
WEBSITE  : www.cytron.io
EMAIL    : support@cytron.io

"""
#import necessary libraries
import board
import time
import neopixel #add "neopixel" library into the "lib" folder 

# Initialize the 2 Neopixel RGB LEDs on pin GP25
pixels = neopixel.NeoPixel(board.GP25, 2)

# Clear Neopixel RGB LED
pixels.fill(0)

# Set pixel brightness
pixels.brightness = 0.5

while True:
    # Light up Neopixel RGB LED with red colour
    # The sequence of the colour code is (R,G,B) input range is from 0-255 (decimal)
    pixels.fill((200, 0, 0)) 
    time.sleep(1)
    pixels.fill(0)
    time.sleep(1)
