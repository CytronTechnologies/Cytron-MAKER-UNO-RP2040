"""
DESCRIPTION:
This example code uses Maker Uno RP2040 to control two LEDs with the onboard user button,
turning one LED on and the other off simultaneously while the button is pressed.

AUTHOR   : Cytron Technologies Sdn Bhd
WEBSITE  : www.cytron.io
EMAIL    : support@cytron.io

"""
# Import necessary libraries
import board
import digitalio
import time

# Initialize LEDs on GP0 and GP1 pins
led1 = digitalio.DigitalInOut(board.GP0)
led2 = digitalio.DigitalInOut(board.GP1)

# Set the LED pins as output
led1.direction = digitalio.Direction.OUTPUT
led2.direction = digitalio.Direction.OUTPUT

# Initialize the onboard Maker UNO RP2040 user button (GP2)
btn1 = digitalio.DigitalInOut(board.GP2)
# Configure 'btn1' as an input with a pull-up resistor
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.UP

# Initially, turn on led1 and turn off led2
led1.value = True
led2.value = False

while True:
    if not btn1.value:
        # When the button is pressed, it turns off LED1 and turns on LED2
        led1.value = False
        led2.value = True
    else:
        # If the button is not pressed, set LED1 to on and LED2 to off
        led1.value = True
        led2.value = False