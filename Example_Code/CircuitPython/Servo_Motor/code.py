"""
DESCRIPTION:
This example code will use Maker Uno RP2040 to controll four servo motors that are connected to the onboard servo port.
The servo motors will rotate through the sequence: 0°, 180°, 90°, and back to 0° degrees in a continuous loop.

AUTHOR   : Cytron Technologies Sdn Bhd
WEBSITE  : www.cytron.io
EMAIL    : support@cytron.io

"""
import time
import board
import digitalio
import pwmio
from adafruit_motor import servo

# Create PWMOut objects for the servo pins
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
    #Set servo angle
    angle = 180
    # Update servo angles.
    servo1.angle = servo2.angle = servo3.angle = servo4.angle = angle
    # Change the angle every 1 second.
    time.sleep(1)

    #Set servo angle
    angle = 90
    # Update servo angles.
    servo1.angle = servo2.angle = servo3.angle = servo4.angle = angle
    # Change the angle every 1 second.
    time.sleep(1)
    
    #Set servo angle
    angle = 0
    # Update servo angles.
    servo1.angle = servo2.angle = servo3.angle = servo4.angle = angle
    # Change the angle every 1 second.
    time.sleep(1)
