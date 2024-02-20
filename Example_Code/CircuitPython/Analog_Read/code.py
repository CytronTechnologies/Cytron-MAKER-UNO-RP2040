"""
DESCRIPTION:
This example code will use Maker Uno RP2040 to read analog value from a potentiometer
and display the reading in the REPL panel. This code applicable to any analog sensor.

CONNECTION:

GP27 - OUT pin of the potentiometer

AUTHOR   : Cytron Technologies Sdn Bhd
WEBSITE  : www.cytron.io
EMAIL    : support@cytron.io

"""
#Import necessary libraries
import board
import time
import analogio

#Define analog pin GP27 used on the board
sensor = analogio.AnalogIn(board.A4)

while True:
    #Serial print the sensor value every 1 second
    raw_value = sensor.value
    voltage_value = (raw_value * 3.3) / 65536
    print('Raw Value : ', raw_value)
    print('Voltage Value : ', voltage_value)
    print('-------------------------')
    time.sleep(1)