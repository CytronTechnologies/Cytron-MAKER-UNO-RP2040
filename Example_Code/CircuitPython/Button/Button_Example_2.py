"""
DESCRIPTION:
This example code uses Maker Uno RP2040 to control two LEDs with the onboard user button.
The initial state has LED1 on and LED2 off. Pressing the button toggles the state of both LEDs.

AUTHOR  : Cytron Technologies Sdn Bhd
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

# Initialize button on GP2
btn1 = digitalio.DigitalInOut(board.GP2)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.UP

# Initially, turn on LED1 and turn off LED2
led1.value = True
led2.value = False

# Track the previous state of the button (initially unpressed)
# 'True' since the button is pulled up
previous_btn_state = True

while True:
    # Read the current state of the button
    current_btn_state = not btn1.value  # Invert the value since it's pulled up

    # Check if the button state has changed (pressed or released)
    if current_btn_state != previous_btn_state:
        if current_btn_state:  # Button is released
            # Toggle the state of LEDs
            led1.value = not led1.value
            led2.value = not led2.value

    # Update the previous button state for the next iteration
    previous_btn_state = current_btn_state