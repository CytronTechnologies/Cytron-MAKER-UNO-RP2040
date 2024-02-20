"""
DESCRIPTION:
This example code will use Maker Uno RP2040 to control four servo motors that are connected to the onboard servo port.
In this code, we will manipulate the sweeping speed of the servo motors.

AUTHOR  : Cytron Technologies Sdn Bhd
WEBSITE  : www.cytron.io
EMAIL    : support@cytron.io

"""
import time
import board
import digitalio
import pwmio
from adafruit_motor import servo

# create a PWMOut object on the control pin.
pwm1 = pwmio.PWMOut(board.GP14, duty_cycle=0, frequency=50)
pwm2 = pwmio.PWMOut(board.GP15, duty_cycle=0, frequency=50)
pwm3 = pwmio.PWMOut(board.GP16, duty_cycle=0, frequency=50)
pwm4 = pwmio.PWMOut(board.GP17, duty_cycle=0, frequency=50)

# Initialize Servo objects.

# A servo might need to be calibrated to get an accurate servo angle.
# Create a Servo object with a min_pulse and max_pulse to calibrated the angle.
# min_pulse should be where the 0° starts while max_pulse should be where 180° stops.
# The pulse range is 750 - 2250 by default (if not defined).
servo1 = servo.Servo(pwm1, min_pulse=580, max_pulse=2700)
servo2 = servo.Servo(pwm2, min_pulse=580, max_pulse=2700)
servo3 = servo.Servo(pwm3, min_pulse=580, max_pulse=2700)
servo4 = servo.Servo(pwm4, min_pulse=580, max_pulse=2700)
angle = 0

while True:
    # Reduce the sleep time between each angle increment to increase sweep speed.
    
    for angle in range(0, 180, 5):
        servo1.angle = angle
        time.sleep(0.05) 

    time.sleep(0.5)

    for angle in range(0, 180, 5):
        servo2.angle = angle
        time.sleep(0.03)  

    time.sleep(0.5)

    for angle in range(0, 180, 5):
        servo3.angle = angle
        time.sleep(0.02)  

    time.sleep(0.5)

    for angle in range(0, 180, 5):
        servo4.angle = angle
        time.sleep(0.01)  

    time.sleep(0.5)
    
    
