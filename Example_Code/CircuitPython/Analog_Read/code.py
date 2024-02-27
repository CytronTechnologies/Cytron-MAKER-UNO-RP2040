"""
DESCRIPTION:
This example code will use Maker Uno RP2040 to read analog value from Maker Soil Module
and display the reading in the REPL panel. This code applicable to any analog sensor.

CONNECTION:

Grove 5 of Maker Uno RP2040 : Maker Soil Module

GP29 - OUT pin of the Maker Soil Module

AUTHOR   : Cytron Technologies Sdn Bhd
WEBSITE  : www.cytron.io
EMAIL    : support@cytron.io

"""
#Import necessary libraries
import board
import time
import analogio

#Define analog pin GP29 used on the board
sensor = analogio.AnalogIn(board.GP29)

while True:
    #Serial print the sensor value every 1 second
    raw_value = sensor.value
    voltage_value = (raw_value * 3.3) / 65536
    print('Raw Value : ', raw_value)
    print('Voltage Value : ', voltage_value)
    print('-------------------------')
    time.sleep(1)
