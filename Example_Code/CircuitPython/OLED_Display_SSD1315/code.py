"""
DESCRIPTION:
This example code demonstrate how to use Maker Uno RP2040 with OLED Display SSD1315 to display text.

CONNECTION:

Grove 6 of Maker UNO RP2040 - Oled Grove 
GP20 - SDA
GP21 - SCL

AUTHOR   : Cytron Technologies Sdn Bhd
WEBSITE  : www.cytron.io
EMAIL    : support@cytron.io

"""
#Import necessary libraries
import board
import busio
import time
import adafruit_ssd1306 #add "adafruit_ssd1306" library into the lib folder

# Define the i2c GPIOs on GP21 and GP20, format: (board.SCL, board.SDA)
i2c = busio.I2C(board.SCL, board.SDA) # can also be written as its pin, GP21 and GP20

# Define the OLED display using the above pins
# format: (width, length, i2c pins)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

while True:
    
    # Clear the OLED display
    oled.fill(0)
    
    # Write the data: ('text', x , y, pixel colour)
    # Pixel colour: 0 = false, 1 = true
    oled.text('Hello world!', 0, 0, 1)
    oled.text('Yeah!', 0, 25, 1)
    
    # Show the written data
    oled.show()
    time.sleep(1)

