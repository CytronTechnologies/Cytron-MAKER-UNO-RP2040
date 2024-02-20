"""
DESCRIPTION:
This example code use Maker Uno RP2040 play melody from the onboard buzzer using PWM output.
Using PWM, we can control the volume of the tone by manupulating the duty_cycle.
In this code, we also create a library of notes for easy access to musical tones.

AUTHOR  : Cytron Technologies Sdn Bhd
WEBSITE  : www.cytron.io
EMAIL    : support@cytron.io

"""
#Import necessary libraries
import board
import digitalio
import time
import pwmio # Add the 'pwmio' library into the 'lib' folder

# Create a PWMOut object for the buzzer pin with variable frequency support.
tone = pwmio.PWMOut(board.BUZZER, variable_frequency=True) #or board.GP8

# Manupulate the duty_cycle to controll the intensity or the volume of the tone.
volume = 100
tone.duty_cycle = volume #32760 is full volume

# Create a library of notes with its corresponding frequency
tones = {
"B0": 31,
"C1": 33,
"CS1": 35,
"D1": 37,
"DS1": 39,
"E1": 41,
"F1": 44,
"FS1": 46,
"G1": 49,
"GS1": 52,
"A1": 55,
"AS1": 58,
"B1": 62,
"C2": 65,
"CS2": 69,
"D2": 73,
"DS2": 78,
"E2": 82,
"F2": 87,
"FS2": 93,
"G2": 98,
"GS2": 104,
"A2": 110,
"AS2": 117,
"B2": 123,
"C3": 131,
"CS3": 139,
"D3": 147,
"DS3": 156,
"E3": 165,
"F3": 175,
"FS3": 185,
"G3": 196,
"GS3": 208,
"A3": 220,
"AS3": 233,
"B3": 247,
"C4": 262,
"CS4": 277,
"D4": 294,
"DS4": 311,
"E4": 330,
"F4": 349,
"FS4": 370,
"G4": 392,
"GS4": 415,
"A4": 440,
"AS4": 466,
"B4": 494,
"C5": 523,
"CS5": 554,
"D5": 587,
"DS5": 622,
"E5": 659,
"F5": 698,
"FS5": 740,
"G5": 784,
"GS5": 831,
"A5": 880,
"AS5": 932,
"B5": 988,
"C6": 1047,
"CS6": 1109,
"D6": 1175,
"DS6": 1245,
"E6": 1319,
"F6": 1397,
"FS6": 1480,
"G6": 1568,
"GS6": 1661,
"A6": 1760,
"AS6": 1865,
"B6": 1976,
"C7": 2093,
"CS7": 2217,
"D7": 2349,
"DS7": 2489,
"E7": 2637,
"F7": 2794,
"FS7": 2960,
"G7": 3136,
"GS7": 3322,
"A7": 3520,
"AS7": 3729,
"B7": 3951,
"C8": 4186,
"CS8": 4435,
"D8": 4699,
"DS8": 4978
}

# Create a list of notes of a song/melody you want play with their respective durations for each note.
MELODY_NOTE = ["E5", "E5", 0,"E5", 0, "C5", "E5", 0, "G5",0] 
MELODY_DURATION = [0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.4,0.5]

while True: #repeat the melody, remove if want to play it once
    
     for i in range(len(MELODY_NOTE)):
       #The boad will not work with 0 frequency, so everytime the frequency is 0, it will rest for a duration of time
       if MELODY_NOTE[i] == 0:
           time.sleep(MELODY_DURATION[i])
       else:
        # Play melody tones
           tone.frequency = tones[MELODY_NOTE[i]]
           tone.duty_cycle = volume  
           time.sleep(MELODY_DURATION[i])
           tone.duty_cycle = 0  # Turn off the buzzer after playing