"""
DESCRIPTION:
This example code use Maker Uno RP2040 and the simpleio library to play tones from a buzzer.
A push button also used to play specific musical notes through the buzzer.

AUTHOR  : Cytron Technologies Sdn Bhd
WEBSITE  : www.cytron.io
EMAIL    : support@cytron.io

"""
#Import necessary libraries
import board
import digitalio
import time
import simpleio # Add the 'simpleio' library to the 'lib' folder

# Define the melody notes with their respective durations
MELODY_NOTE = [659, 659, 0, 659, 0, 523, 659, 0, 784] # [E5, E5, REST, E5, REST, C5, E5, REST, G5]
MELODY_DURATION = [0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.2]

# Define pin connected to piezo buzzer
PIEZO_PIN = board.BUZZER #or board.GP8

#Initialize buttons
btn = digitalio.DigitalInOut(board.GP2)
btn.direction = digitalio.Direction.INPUT
btn.pull = digitalio.Pull.UP

# Play melody during start up  
for i in range(len(MELODY_DURATION)):
    #The boad will not work with 0 frequency, so everytime the frequency is 0, it will rest for a duration of time
    if MELODY_NOTE[i] == 0:
        time.sleep(MELODY_DURATION[i])
    else:
        # Play melody tones
        simpleio.tone(PIEZO_PIN, MELODY_NOTE[i], duration=MELODY_DURATION[i])

while True:
    # Check if button (GP2) is pressed
    if not btn.value:
        # Play tones
        # Format(pin,frequency,duration)
        simpleio.tone(PIEZO_PIN, 262, duration=0.1)
        simpleio.tone(PIEZO_PIN, 659, duration=0.15)
        simpleio.tone(PIEZO_PIN, 784, duration=0.2)
        