"""
DESCRIPTION:
This example code will shoqw how to use the Maker Uno RP2040's onboard buzzer to play tones and melody.

AUTHOR   : Cytron Technologies Sdn Bhd
WEBSITE  : www.cytron.io
EMAIL    : support@cytron.io

"""
# Import necessary libraries
from machine import Pin, PWM
import time

# Define the melody note frequency with its corresponding duration
MELODY_NOTE = [659, 659, 0, 659, 0, 523, 659, 0, 784]
MELODY_DURATION = [0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.2]

volume = 500 # Maximum is 65535. Adjust as needed

# Initialize a buzzer using PWM on Pin 8
buzzer = PWM(Pin(8))

# Initialize button 1 as input with pull-up resistor
btn1 = Pin(2, Pin.IN, Pin.PULL_UP)

# Play the pre-defined melody 
for i in range(len(MELODY_DURATION)):
    # Check if the note is a rest (frequency = 0)
    if MELODY_NOTE[i] == 0:
         buzzer.duty_u16(0)
    else:
        # Play melody tones
        buzzer.freq(MELODY_NOTE[i])
        buzzer.duty_u16(volume)
    time.sleep(MELODY_DURATION[i])
# Turn off the buzzer after playing the melody
buzzer.duty_u16(0)

while True:
    # Check button (GP20) is pressed
    if not btn1.value():
        # Play tones
        # Format(pin,frequency,duration)
        buzzer.freq(262)
        buzzer.duty_u16(volume)
        time.sleep(0.1)
        buzzer.freq(659)
        buzzer.duty_u16(volume)
        time.sleep(0.1)
        buzzer.freq(784)
        buzzer.duty_u16(volume)
        time.sleep(0.1)
        # Turn off the buzzer
        buzzer.duty_u16(0)