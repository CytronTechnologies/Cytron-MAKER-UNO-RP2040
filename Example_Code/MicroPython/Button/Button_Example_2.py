"""
DESCRIPTION:
This example code will how to use/program the User push button on the Maker Uno RP2040.
In this code each button press, will light specific onboard LED acting like a visual counter.
After the 4th press, the counter will reset to 0.

AUTHOR   : Cytron Technologies Sdn Bhd
WEBSITE  : www.cytron.io
EMAIL    : support@cytron.io

The User Button is internally connected to GP2 

"""
# Import necessary libraries
from machine import Pin
import time

# Create individual Pin objects for each LED
led1 = Pin(0, Pin.OUT)
led2 = Pin(1, Pin.OUT)
led3 = Pin(2, Pin.OUT)

# Create a Pin object for the button as an input with a pull-up resistor
button = Pin(21, Pin.IN, Pin.PULL_UP)

# Initialize LED states to low
led1.value(False)
led2.value(False)
led3.value(False)

# Variable to count button presses, starts with zero count
press_count = 0

# Infinite loop to monitor the button presses
while True:
    
    # Check if the button is pressed
    if not button.value(): #if not, since the button pin is pulled high
        
        # Increment the press count
        press_count += 1
        
         # Handle different cases based on the button count
        if press_count == 1:
            led1.value(True)  # Turn on LED1
        elif press_count == 2:
            led2.value(True)  # Turn on LED2
        elif press_count == 3:
            led3.value(True)  # Turn on LED3
        elif press_count == 4:
            # If 4 button presses have occurred, turn off all LEDs and reset the count
            led1.value(False)
            led2.value(False)
            led3.value(False)
            press_count = 0
        
        # Wait for a short duration
        time.sleep(0.5)