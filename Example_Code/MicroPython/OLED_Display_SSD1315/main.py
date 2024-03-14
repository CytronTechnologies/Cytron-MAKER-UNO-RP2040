"""
DESCRIPTION:
This example code uses Maker Uno RP2040 to display text on the OLED Display SSD1315.

CONNECTION:
Maker UNO RP2040 GROVE 6 with OLED Display Grove
GP20 - SDA
GP21 - SCL

AUTHOR   : Cytron Technologies Sdn Bhd
WEBSITE  : www.cytron.io
EMAIL    : support@cytron.io

"""
# Import necessary libraries
# Ensure the "ssd1306" library is uploaded to the board
from machine import Pin, SoftI2C
import ssd1306
import framebuf
import time


# Initialize SoftI2C with SDA on Pin 20 and SCL on Pin 21
#format: (board.SCL, board.SDA)
i2c = SoftI2C(scl=Pin(21), sda=Pin(20))   


# Initialize SSD1306 display with 128x64 resolution using the I2C interface
#format: (width, length, i2c pins)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

while True:
    
    #Clear the OLED display
    oled.fill(0)
    
    # Write the data: ('text', x , y, pixel colour)
    #pixel colour: 0 = false, 1 = true
    oled.text('Hello world!', 0, 0, 1)
    oled.text('Yeah!', 0, 25, 1)
    
    #Show the written data
    oled.show()
    time.sleep(1)
