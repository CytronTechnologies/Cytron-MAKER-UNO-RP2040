"""
DESCRIPTION:
This example code will how to use/program the User push button on the Maker Uno RP2040.
In this code, the user button will serve as a input to control the condition of two onboard LEDs.

AUTHOR   : Cytron Technologies Sdn Bhd
WEBSITE  : www.cytron.io
EMAIL    : support@cytron.io

The User button is internally connected to GP2

"""
# Import necessary libraries
from machine import Pin
import time

# Define Pin 0 and Pin 1 as outputs for the LEDs
led1 = Pin(0, Pin.OUT)
led2 = Pin(1, Pin.OUT)

# Define Pin 2 as an input with a pull-up resistor for the button
btn1 = Pin(2, Pin.IN, Pin.PULL_UP)

led1.value(False) #Set initial condition for led1 to low
led2.value(True)  #Set initial condition for led1 to high

while True:
    # Check if button1 (GP2) is pressed 
    if not btn1.value():
        
        # Turn on LED1 and turn off LED2
        led1.value(True)
        led2.value(False)
        time.sleep(0.5)
        
        # Turn off LED1 and turn on LED2
        led1.value(False)
        led2.value(True)