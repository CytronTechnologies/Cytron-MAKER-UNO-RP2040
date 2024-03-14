"""
DESCRIPTION:
This example code uses the Maker Uno RP2040 with four servo motors connected to its servo ports
to demonstrate basic servo motor control. 

AUTHOR   : Cytron Technologies Sdn Bhd
WEBSITE  : www.cytron.io
EMAIL    : support@cytron.io

"""
# Import necessary libraries
import time
from machine import Pin, PWM

# Create PWM objects on the control pin for each servo motor
pwm1 = PWM(Pin(14))
pwm2 = PWM(Pin(15))
pwm3 = PWM(Pin(16))
pwm4 = PWM(Pin(17))

# Set the frequency of all PWM signals to 50 Hz
pwm1.freq(50)
pwm2.freq(50)
pwm3.freq(50)
pwm4.freq(50)

# Initialize variables for controlling servo angles and duty cycles
# The dutycycle values (2200-8300) represent the servo angles from 0 to 180 degrees
# You might need to calibrate the min_dutycycle (pulse at 0 degrees) and max_dutycycle (pulse at 180 degrees) to get an accurate servo angle.
angle = 0.0
min_dutycycle = 2200
max_dutycycle = 8300
dutycycle = 0

while True:
    # Set the servo angles to 180 degree
    angle = 180
    # Calculate the corresponding duty cycle based on the angle
    dutycycle = int(((max_dutycycle - min_dutycycle) / 180) * angle) + min_dutycycle
    # Set the duty cycle for all servo motors
    pwm1.duty_u16(dutycycle)
    pwm2.duty_u16(dutycycle)
    pwm3.duty_u16(dutycycle)
    pwm4.duty_u16(dutycycle)
    # Change the angle every 1 second.
    time.sleep(1)

    # Set the servo angles to 0 degree
    angle = 0
    # Calculate the corresponding duty cycle based on the angle
    dutycycle = int(((max_dutycycle - min_dutycycle) / 180) * angle) + min_dutycycle
    # Set the duty cycle for all servo motors
    pwm1.duty_u16(dutycycle)
    pwm2.duty_u16(dutycycle)
    pwm3.duty_u16(dutycycle)
    pwm4.duty_u16(dutycycle)
    # Change the angle every 1 second.
    time.sleep(1)
