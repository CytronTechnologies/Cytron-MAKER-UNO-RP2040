/*
DESCRIPTION:
This example code will use Maker UNO RP2040 with Ultrasonic Sensor HC-SR04P
to measure distance and then display the readings on serial monitor. 

CONNECTION:

HC-SR04P - Grove 6 of Maker UNO RP2040
           or 
GP20 - Echo pin of HC-SR04P
GP21 - Trig pin of HC-SR04P

AUTHOR   : Cytron Technologies Sdn Bhd
WEBSITE  : www.cytron.io
EMAIL    : support@cytron.io

REFERENCE:
Code adapted from www.HowToMechatronics.com:
https://howtomechatronics.com/tutorials/arduino/ultrasonic-sensor-hc-sr04/

*/

// defines pins numbers
const int echoPin = 20;
const int trigPin = 21;

// defines variables
long duration;
int distance;

void setup() {
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPin, INPUT); // Sets the echoPin as an Input
  Serial.begin(9600); // Starts the serial communication
}
void loop() {
  // Clears the trigPin
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  // Sets the trigPin on HIGH state for 10 micro seconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // Measure the response from the echoPin
  duration = pulseIn(echoPin, HIGH);

  // Calculate the distance from duration value
  // Use 343 metres per second as the speed of sound

  distance = duration * 0.034 / 2;

  // Prints the distance on the Serial Monitor
  Serial.print("Distance : ");
  Serial.print(distance);
  Serial.println(" cm");
  delay(100);
}