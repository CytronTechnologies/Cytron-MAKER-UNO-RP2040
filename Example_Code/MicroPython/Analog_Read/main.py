"""
DESCRIPTION:
This example code uses the Maker Uno RP2040 with the Maker Soil sensor module to read the analog value
and displays it in the Thonny IDE shell.

This code can also be used with a potentiometer and any other analog sensor.

CONNECTION:

Grove 5 of Maker Uno RP2040 : Maker Soil Module

GP29 - OUT pin of the Maker Soil Module
GP28 - DIS pin (But we will not using this feature in the program)


AUTHOR   : Cytron Technologies Sdn Bhd
WEBSITE  : www.cytron.io
EMAIL    : support@cytron.io

"""

# Import necessary libraries
import machine
import time

# Initialize ADC (Analog-to-Digital Converter) on Pin 27 for sensor/analog input readings
sensor = machine.ADC(27)

while True:
    
    # Read the raw ADC value (16-bit unsigned integer)
    raw_value = sensor.read_u16()
    
    # Convert raw ADC value to voltage using the formula: voltage = (raw_value * Vref) / (2^resolution)
    # In this case, Vref is 3.3V, and resolution is 16 bits (65536 levels)
    voltage_value = (raw_value * 3.3) / 65536
    
    # Print raw and voltage values for monitoring
    # For Maker Soil Sensor, the higher the voltage, the higher the moisture level of the soil. 
    print('Raw Value : ', raw_value)
    print('Voltage Value : ', voltage_value)
    print('-------------------------')
    time.sleep(1)
