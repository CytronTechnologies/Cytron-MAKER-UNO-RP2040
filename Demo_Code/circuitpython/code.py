import board
import digitalio
import time
import pulseio
import pwmio
import neopixel
import busio
import random

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

# Initialize led pins
LED = []
pins = [board.GP1,board.GP0,board.GP3,board.GP4,board.GP5,board.GP6,board.GP7,board.GP9,board.GP13,board.GP11,board.GP12,board.GP10,
        board.GP20,board.GP21]

for pin in pins:
    digout = digitalio.DigitalInOut(pin)
    digout.direction = digitalio.Direction.OUTPUT
    LED.append(digout)
    
shades_of_blue = [(0, 50, 0), (0, 100, 0), (25, 125, 0), (50, 150, 0), (75, 175, 0), (100, 200, 0), (125, 225, 0), (150, 100, 0), (200, 100, 0), (255, 0, 0)]

# RGB Pin
pixel= neopixel.NeoPixel(board.GP25, 2)

# Initialize buzzer
buzzer=pwmio.PWMOut(board.GP8, variable_frequency=True)
volume = 60000
buzzer.duty_cycle = volume

btn1 = digitalio.DigitalInOut(board.GP2)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.UP
# Melody
MELODY_NOTE = ["E5", "E5", 0,"E5", 0, "C5", "E5", 0, "G5",0] 
MELODY_DURATION = [0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.2,0.5]
up = ['E4','D4','C4']


def startup():

    pixel.fill((0,0,0))
    for i in range(5):
        buzzer.duty_cycle = 0
        LED[6-i].value = True
        LED[7+i].value = True
        time.sleep(0.05)
        LED[6-i].value = False
        LED[7+i].value = False
        
    for i in range(len(MELODY_NOTE)):
        LED[2+i].value = True
        play_mario_tone(i, MELODY_NOTE)
        
def ledupbot(Cond):
    for i in [0, 1, 12, 13]:
        LED[i].value = Cond
        

def cond0():
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
        random_index = random.randint(0, len(colors) - 1)
        random_color = colors[random_index]

        for j in range(2, 8):
            LED[j].value = True
            LED[13 - j].value = True
            time.sleep(0.05)
            LED[j].value = False
            LED[13 - j].value = False

            if j == 7:
                pixel.fill(random_color)
                pixel.show()
                
        for i in range(7, 2, -1):
            LED[i].value = True
            LED[13 - i].value = True
            time.sleep(0.05)
            LED[i].value = False
            LED[13 - i].value = False

def cond1():
       
       cond_led(12)
       start_frequency = 400
       end_frequency = 1000
       frequency_step = 50
       time.sleep(0.05)
       pixel.fill(0)
# Loop through the frequency range
       for frequency in range(start_frequency, end_frequency + 1, frequency_step):        
            for k in range(12):
                 LED[k].value = False
            buzzer.frequency=frequency
            buzzer.duty_cycle = volume

# Determine LED index based on frequency
            led_index = frequency_to_led_index(frequency)
            pixel.fill(shades_of_blue[led_index-2])
# Light up LEDs up to the determined LED index
            for k in range(2,led_index+1):
                 pixel.fill(shades_of_blue[k-2])
                 LED[k].value = True
            time.sleep(0.1)
            
       time.sleep(0.3)
       buzzer.duty_cycle = 0
       
def cond2():
       cond_led(13)
       start_frequency = 400
       end_frequency = 1000
       frequency_step = 50
       cond_led(13)
       time.sleep(0.05)
       pixel.fill(0)
       
       for frequency in range(end_frequency, start_frequency - 1, -frequency_step):  
            buzzer.frequency = frequency
            buzzer.duty_cycle = volume
            led_index = frequency_to_led_index(frequency)

            for k in range(2, led_index + 1):
                pixel.fill(shades_of_blue[k-2])
                LED[k].value = True

            for k in range(2, led_index + 1):
                pixel.fill(shades_of_blue[k-2])
                LED[k].value = True

            time.sleep(0.1)

            for k in range(12):
               LED[2].value = False 
               LED[k].value = False
       time.sleep(0.3)
       buzzer.duty_cycle = 0
       
            
def frequency_to_led_index(frequency):
    
    if frequency < 540:
        return 2  # LED 3
    elif frequency < 600:
        return 3  # LED 4
    elif frequency < 650:
        return 4  # LED 5
    elif frequency < 700:
        return 5  # LED 6
    elif frequency < 730:
        return 6  # LED 7
    elif frequency < 780:
        return 7  # LED 9
    elif frequency < 830:
        return 8  # LED 13
    elif frequency < 880:
        return 9  # LED 11
    elif frequency < 930:
        return 10  # LED 12
    else:
        return 11  # LED 10
            

def cond_led(cond):
    LED[12].value = False
    LED[13].value = False
    LED[cond].value = True
    

    

def play_mario_tone(i, notes):

     if MELODY_NOTE[i] == 0:
           time.sleep(MELODY_DURATION[i])
     else:
           if i % 2 == 1:  # Check if the index is even
              pixel[0] = (155, 155, 0) # Yellow color for Neopixel 0
              pixel[1] = (0, 100, 155)
    
           else:
              pixel[0] = (0, 100, 155) # Turn off Neopixel 0
              pixel[1] = (155, 155, 0)
            
           buzzer.frequency = tones[MELODY_NOTE[i]]
           buzzer.duty_cycle = volume
           time.sleep(MELODY_DURATION[i])
           buzzer.duty_cycle = 0
           pixel.fill((0,0,0))
           
buzzer.duty_cycle = 0    
pixel.fill((0,0,0))
startup()
counter = 0
button_pressed = False


while True:
    
    if not btn1.value and not button_pressed:
        counter += 1
        button_pressed = True
        print(counter)
        if counter<3:
            buzzer.frequency = 500*counter
            buzzer.duty_cycle = volume
            time.sleep(0.3)
            buzzer.duty_cycle = 0
            time.sleep(0.1)
    elif btn1.value:
        button_pressed = False


    if counter ==0:
       cond0()
       cond1_executed = False
       cond2_executed = False
       
    elif counter == 1 and not cond1_executed:
       
       time.sleep(0.2)
       cond1()
       cond1_executed = True
    
    elif counter == 2 and not cond2_executed:
       
       
       time.sleep(0.2)
       cond2()
       cond2_executed = True
       pixel.fill((0,0,0))
    
    elif counter ==3:
       LED[13].value = False
       LED[12].value = False
       counter=0   
