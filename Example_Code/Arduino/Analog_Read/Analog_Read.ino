/*
DESCRIPTION:
This example code will use Maker Uno RP2040 to read the analog input from Maker Soil Module
and then show the result on serial monitor. This code also applicable to any analog sensor.

CONNECTION:

Grove 5 of Maker Uno RP2040 : Maker Soil Module
GP29 - OUT pin of the Maker Soil Module

AUTHOR   : Cytron Technologies Sdn Bhd
WEBSITE  : www.cytron.io
EMAIL    : support@cytron.io
*/

int sensorPin = 29;    // select the input pin for the potentiometer
int raw_value = 0; 
float voltage_value = 0; 

void setup() {
  // declare the sensorPin as an OUTPUT:
  pinMode(sensorPin, INPUT);
  Serial.begin(9600);
  // enable adc resolution to 12-bit (default 10-bit)
  analogReadResolution(12);
}

void loop() {

  // read the value from the sensor:
  raw_value = analogRead(sensorPin);
  // Convert the raw ADC value to voltage (3.3V is the board's voltage reference)
  voltage_value = (raw_value * 3.3) / 4095;
  
  Serial.print("Raw Value : ");
  Serial.println(raw_value);
  Serial.print("Voltage Value : ");
  Serial.println(voltage_value);
  Serial.println("---------------------------");
  
  delay(1000);
}
