'''
Demo-Code for MAKER-UNO-RP2040
This demo code is written in CircuitPython and it serves
as an easy quality check when you first receive the board.

Upon powering up (slide power switch to ON), a series of blue LEDs
will light up in a visual countdown pattern. Then, a short melody
will be played,with the NeoPixel alternately lighting up in blue
and yellow, and the servo motors sweeping to 180 degrees.

After that, the blue LEDs will animate in two parts:one half will
light up sequentially from the bottom to the top, while the other
half will do the same from the top to the bottom. When they meet
in the middle, the RGB LED will lights random color. At the same
time, the servos will sweep from 50 degrees to 0 degrees. This
action will happen in a repeating loop while the program checks
the push button's state. Each button press triggers different
action.

First Press:
The board will plays an ascending note in one and , where each note
corresponds to different LED numbers, RGB LED colors, and servo
positions, creating a visual and auditory experience. As the note
gets higher, more LEDs light up in the series. For the RGB LED,
the color changes from green to yellow to red. The servo angle also
changes from 0 to 180 degrees, with higher notes corresponding to
higher angles.
 
Second Press:
The board plays the notes and corresponding actions in reverse,
starting from the highest to the lowest.

After the third press, the board resets to zero button presses.

'''

import board
import digitalio
import time
import pulseio
import pwmio
import neopixel
import busio
import random
import pwmio
from adafruit_motor import servo, motor

# Create a dictionary of notes with its corresponding frequencies.
tones = {
    '0':    1,
    'B0':  31,
    'C1':  33,
    'CS1': 35,
    'D1':  37,
    'DS1': 39,
    'E1':  41,
    'F1':  44,
    'FS1': 46,
    'G1':  49,
    'GS1': 52,
    'A1':  55,
    'AS1': 58,
    'B1':  62,
    'C2':  65,
    'CS2': 69,
    'D2':  73,
    'DS2': 78,
    'E2':  82,
    'F2':  87,
    'FS2': 93,
    'G2':  98,
    'GS2': 104,
    'A2':  110,
    'AS2': 117,
    'B2':  123,
    'C3':  131,
    'CS3': 139,
    'D3':  147,
    'DS3': 156,
    'E3':  165,
    'F3':  175,
    'FS3': 185,
    'G3':  196,
    'GS3': 208,
    'A3':  220,
    'AS3': 233,
    'B3':  247,
    'C4':  262,
    'CS4': 277,
    'D4':  294,
    'DS4': 311,
    'E4':  330,
    'F4':  349,
    'FS4': 370,
    'G4':  392,
    'GS4': 415,
    'A4':  440,
    'AS4': 466,
    'B4':  494,
    'C5':  523,
    'CS5': 554,
    'D5':  587,
    'DS5': 622,
    'E5':  659,
    'F5':  698,
    'FS5': 740,
    'G5':  784,
    'GS5': 831,
    'A5':  880,
    'AS5': 932,
    'B5':  988,
    'C6':  1047,
    'CS6': 1109,
    'D6':  1175,
    'DS6': 1245,
    'E6':  1319,
    'F6':  1397,
    'FS6': 1480,
    'G6':  1568,
    'GS6': 1661,
    'A6':  1760,
    'AS6': 1865,
    'B6':  1976,
    'C7':  2093,
    'CS7': 2217,
    'D7':  2349,
    'DS7': 2489,
    'E7':  2637,
    'F7':  2794,
    'FS7': 2960,
    'G7':  3136,
    'GS7': 3322,
    'A7':  3520,
    'AS7': 3729,
    'B7':  3951,
    'C8':  4186,
    'CS8': 4435,
    'D8':  4699,
    'DS8': 4978,
}

# Initialize led pins.
# Create a list for led pins.
LED = []
pins = [board.GP1,board.GP0,board.GP3,board.GP4,board.GP5,board.GP6,board.GP7,board.GP9,board.GP13,board.GP11,board.GP12,board.GP10,
        board.GP20,board.GP21]

# Configure the pin as digital outputs and store them in the LED list.
for pin in pins:
    digout = digitalio.DigitalInOut(pin)
    digout.direction = digitalio.Direction.OUTPUT
    LED.append(digout)
    
# Create an array and add servo objects.
servo_motors = []
servo_motors.append(servo.Servo(pwmio.PWMOut(board.GP14, duty_cycle=0, frequency=50)))
servo_motors.append(servo.Servo(pwmio.PWMOut(board.GP15, duty_cycle=0, frequency=50)))
servo_motors.append(servo.Servo(pwmio.PWMOut(board.GP16, duty_cycle=0, frequency=50)))
servo_motors.append(servo.Servo(pwmio.PWMOut(board.GP17, duty_cycle=0, frequency=50)))
    
green_to_red = [(0, 50, 0), (0, 100, 0), (25, 125, 0), (50, 150, 0), (75, 175, 0), (100, 200, 0), (125, 225, 0), (150, 100, 0), (200, 100, 0), (255, 0, 0)]

# Initialize a NeoPixel object named 'pixel' on pin GP25 with 2 pixels (2 LEDs).
pixel= neopixel.NeoPixel(board.GP25, 2)

# Initialize a PWMOut object named 'buzzer' on pin GP8 with variable frequency.
buzzer=pwmio.PWMOut(board.GP8, variable_frequency=True)

# Set the duty cycle of the buzzer (Volume)
volume = 60000
buzzer.duty_cycle = volume

# Configure a digital input button (btn) connected to GPIO pin 2 with a pull-up resistor.
btn = digitalio.DigitalInOut(board.GP2)
btn.direction = digitalio.Direction.INPUT
btn.pull = digitalio.Pull.UP

# Define the melody notes with its corresponding duration (Mario theme song).
MELODY_NOTE = ["E5", "E5", 0,"E5", 0, "C5", "E5", 0, "G5",0] 
MELODY_DURATION = [0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.2,0.5]

# Define an octave with its corresponding durations.
octave = ["C4", "D4", "E4", "F4", "G4", "A4", "B4", "C5", "D5","E5" ]
octave_duration = [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.5]

# On startup function
def startup():
    
    # Turn off the NeoPixel (pixel) and set all servo motors to 180 degrees.
    pixel.fill((0,0,0)) # 
    for k in range(len(servo_motors)):
            servo_motors[k].angle = 180
            
    # Leds visual animation (Visual Coundown)        
    for i in range(5):
        buzzer.duty_cycle = 0
        LED[6-i].value = True
        LED[7+i].value = True
        time.sleep(0.05)
        LED[6-i].value = False
        LED[7+i].value = False
    
    # Reset servo motors to 0 degrees and play a melody (Mario theme song).
    for k in range(len(servo_motors)):
        servo_motors[k].angle = 0
    for i in range(len(MELODY_NOTE)):
        LED[2+i].value = True
        play_mario_tone(i, MELODY_NOTE)
    
# Funtion for condition 0    
def cond0():
        
        # Define a list of colors
        colors = [
                (200, 0, 0),
                (0, 200, 0),
                (0, 0, 200),
                (0, 200, 200),
                (255, 255, 0),
                (128, 0, 128),
                (0, 128, 128),
                (255, 0, 255),
                (0, 128, 255),
                (255, 128, 0),
                (128, 255, 0),
                (0, 255, 128),
        ]
        # Select a random color from the list
        random_index = random.randint(0, len(colors) - 1)
        random_color = colors[random_index]
       
        # Set servo motors to 50 degrees
        for k in range(len(servo_motors)):
            servo_motors[k].angle = 50
        
        # Led visual animation
        for j in range(2, 8):
            LED[j].value = True
            LED[13 - j].value = True
            time.sleep(0.05)
            LED[j].value = False
            LED[13 - j].value = False
            
            # When reaching the center LED, fill the NeoPixel with a random color.
            if j == 7:
                pixel.fill(random_color)
                pixel.show()
                
        # Reset servo motors to 0 degrees and blink LEDs in reverse order
        for k in range(len(servo_motors)):
            servo_motors[k].angle = 0                
        for i in range(7, 2, -1):
            LED[i].value = True
            LED[13 - i].value = True
            time.sleep(0.05)
            LED[i].value = False
            LED[13 - i].value = False
            
# Function for Condition 1
# Play notes from the 'octave' list in ascending order.
def cond1():
    
    for i in range(len(octave)):
            
            # Play notes from the 'octave' list with specified volume
            buzzer.frequency = tones[octave[i]] 
            buzzer.duty_cycle = volume
            # Turn on the LED corresponding to the current note.
            LED[i+2].value = True
            # Set the NeoPixel color to the shade of blue corresponding to the current note.
            pixel.fill(green_to_red[i])
            # Wait for the duration of the current note.
            time.sleep(octave_duration[i])
            # Set the angle of all servo motors based on the current note.
            for k in range(len(servo_motors)):
                servo_motors[k].angle = (i / 10) * 180
           
    buzzer.duty_cycle =0

# Function for Condition 2
# Play notes from the 'octave' list in descending order.
def cond2():
  
  # Play notes from the 'octave' list
  for i in range(len(octave) - 1, -1, -1):
      buzzer.frequency = tones[octave[i]]
      buzzer.duty_cycle = volume
      LED[i+2].value = False # Turn on the LED corresponding to the current note.
      pixel.fill(green_to_red[i])  # Set the NeoPixel color to the shade of blue corresponding to the current note.
      time.sleep(octave_duration[len(octave) - 1 - i])
      for k in range(len(servo_motors)):
           servo_motors[k].angle = (i / 10) * 180
      
  buzzer.duty_cycle =0


# Function for condition LED 
def cond_led(cond):
    # LED 21 and LED 22 act indicator led to indicate then current counter/condition state (LED n-12 and 13 from the LED list)
    # LED 21 is on if condition 1 is running
    # LED 22 is on if condition 1 is running
    LED[12].value = False
    LED[13].value = False
    LED[cond].value = True

 
# Function to play mario theme song
def play_mario_tone(i, notes):
     
     # Check if the note frequency is 0 (rest)
     if MELODY_NOTE[i] == 0:
           # If 0, wait for the duration of the rest (silent)
           time.sleep(MELODY_DURATION[i])
     #if the note is not 0, play the note
     else:
           # Check if the note index is odd number to set the left RGB LED to yellow and right RGB LED to blue
           # or even to set left RGB LED to blue and right RGB LED to yellow
           if i % 2 == 1:
              pixel[0] = (155, 155, 0) # Yellow color for pixel 0
              pixel[1] = (0, 100, 155) # Blue color for pixel 1
    
           else:
              pixel[0] = (0, 100, 155) # Blue color for pixel 0
              pixel[1] = (155, 155, 0) # Yellow color for pixel 0
           # Set the buzzer frequency to play the current note with the specified volume
           buzzer.frequency = tones[MELODY_NOTE[i]]
           buzzer.duty_cycle = volume
           # Wait for the duration of the note
           time.sleep(MELODY_DURATION[i])
           # Turn off buzzer after each each note duration finished
           buzzer.duty_cycle = 0
           # Turn off both RGB LED
           pixel.fill((0,0,0))


# Stop buzzer and turn off NeoPixel to prepare for startup code
buzzer.duty_cycle = 0    
pixel.fill((0,0,0))

# Run startup code
startup()

# Initialize variables 
counter = 0            # Keeps track of the number of button presses
button_pressed = False # Flag to indicate if the button is pressed

while True:

# --------------------------------------------------------------------------------------------
# Check if button is pressed (btn.value is False when pressed since the button is pulled high)
# and if the button is not being pressed before
# this condition is to prevent the action from repeating while the button is held down
# ---------------------------------------------------------------------------------------------
    if not btn.value and not button_pressed:
        # Increase the counter by 1 when button is pressed
        counter += 1
        # set button_pressed condition to true
        button_pressed = True
        print(counter)
        
        # Play tone based on the button press counter
        # Each counter/condition have different tone
        if counter<3:
            buzzer.frequency = 500*counter
            buzzer.duty_cycle = volume
            time.sleep(0.3)
            buzzer.duty_cycle = 0
            time.sleep(0.1)
    elif btn.value:
        button_pressed = False

# -------------------------------------------------------------- #
# Execute different conditions based on the button press counter #
# -------------------------------------------------------------- #

    # When counter is 0
    if counter ==0:
       # Execute condition 0
       cond0() 
       # Reset flags for condition execution to indicate that condition 1 and 2 have not been executed
       # this because to make sure condition 1 and 2 can be executed again in the next cycle
       cond1_executed = False
       cond2_executed = False
       
    # When counter is 1 and cond1 has not been executed yet
    elif counter == 1 and not cond1_executed:
       time.sleep(0.2)
       cond1()
       # Set flag to indicate that cond1 has been executed
       # this is to prevent cond1 from being executed again in same cycle
       cond1_executed = True
    
    # When counter is 2 and cond2 has not been executed yet
    elif counter == 2 and not cond2_executed:
       time.sleep(0.2)
       cond2()
       # Set flag to indicate that cond2 has been executed
       # this is to prevent cond2 from being executed again in same cycle
       cond2_executed = True
       # Turn RGB LED
       pixel.fill((0,0,0))
    
    # When counter is 3
    elif counter ==3:
       # Reset "condition" LEDs
       LED[13].value = False
       LED[12].value = False
       # Reset counter to 0 for next cycle
       counter=0   

