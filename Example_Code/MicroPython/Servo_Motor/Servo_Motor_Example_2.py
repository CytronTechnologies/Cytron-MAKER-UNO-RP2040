"""
DESCRIPTION:
This example code uses the Maker Uno RP2040 to control four servo motors connected to its servo ports.
The code continuously adjusts the servo angles in a range from 0 to 180 degrees, creating a sweeping motion.

AUTHOR   : Cytron Technologies Sdn Bhd
WEBSITE  : www.cytron.io
EMAIL    : support@cytron.io

"""
import time
from machine import Pin, PWM

# Create PWM objects for each servo motor on their respective control pins
pwm1 = PWM(Pin(12))
pwm2 = PWM(Pin(13))
pwm3 = PWM(Pin(14))
pwm4 = PWM(Pin(15))
# Set the frequency of all PWM signals to 50 Hz.
pwm1.freq(50)
pwm2.freq(50)
pwm3.freq(50)
pwm4.freq(50)

# Define the initial servo angle, duty cycle range for 0-180 degrees, and increment direction
angle = 0.0
min_dutycycle = 2200
max_dutycycle = 8300
dutycycle = 0
add_angle = True

while True:
    # Condition to add or subtract angle based on limits
    if angle <= 0:
        add_angle = True
    if angle >= 180:
        add_angle = False
        
    # Increment or decrement the angle based on the condition  
    if add_angle:
        angle += 5
    else:
        angle -= 5
    
    # Calculate duty cycle based on the angle
    dutycycle = int(((max_dutycycle - min_dutycycle) / 180) * angle) + min_dutycycle
    # Update servo angles.
    pwm1.duty_u16(dutycycle)
    pwm2.duty_u16(dutycycle)
    pwm3.duty_u16(dutycycle)
    pwm4.duty_u16(dutycycle)
    # Change the angle every 0.5 second.
    time.sleep(0.5)
