"""
DESCRIPTION:
This example code will use Maker Uno RP2040 to light up two onboard LED alternately.
For this code, GPIO LEDs of the GP0 and GP1 are selected

AUTHOR   : Cytron Technologies Sdn Bhd
WEBSITE  : www.cytron.io
EMAIL    : support@cytron.io

"""
#import necessary libraries
import board
import digitalio
import time

#initialize leds on GP0 and GP1 pins
led1 = digitalio.DigitalInOut(board.GP0)
led2 = digitalio.DigitalInOut(board.GP1)

#set the led pins as output
led1.direction = digitalio.Direction.OUTPUT
led2.direction = digitalio.Direction.OUTPUT

while True:
    #led1 is light up for 0.5s then turned off
    led1.value = True
    time.sleep(0.5)
    led1.value = False
    time.sleep(0.5)

    #led2 is light up for 0.5s then turned off
    led2.value = True
    time.sleep(0.5)
    led2.value = False
    time.sleep(0.5)

