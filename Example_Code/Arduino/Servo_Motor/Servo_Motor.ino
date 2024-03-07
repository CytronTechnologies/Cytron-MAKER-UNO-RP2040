/*
DESCRIPTION:
This example code will use Maker UNO RP2040 to control four servo motors connected to the onboard servo ports

AUTHOR   : Cytron Technologies Sdn Bhd
WEBSITE  : www.cytron.io
EMAIL    : support@cytron.io
*/

  // Include the servo library
#include <Servo.h>

  // Create servo objects for each servos
Servo servo1;  
Servo servo2;
Servo servo3;
Servo servo4;

void setup() {

  // Attach each servo object to their corresponding pins
  servo1.attach(14);  
  servo2.attach(15);
  servo3.attach(16);
  servo4.attach(17);
}

void loop() {
  
   // Move the servos from 0 degress to 180 degrees with with an increment of 1 degree per step
  for (int pos = 0; pos <= 180; pos += 1) { 
  servo1.write(pos);     // Set Servo 1 position to 'pos' degrees
  servo2.write(pos);     // Set Servo 2 position to 'pos' degrees
  servo3.write(pos);     // Set Servo 3 position to 'pos' degrees
  servo4.write(pos);     // Set Servo 4 position to 'pos' degrees
  delay(10);  // Pause for 15 milliseconds to control the speed of servo movement
  }
   
   // Move the servos from 180 degress to 0 degrees with with a decrement of 1 degree per step
  for (int pos = 200; pos >= 0; pos -= 1) { 
  servo1.write(pos);     // Set Servo 1 position to 'pos' degrees
  servo2.write(pos);     // Set Servo 2 position to 'pos' degrees
  servo3.write(pos);     // Set Servo 3 position to 'pos' degrees
  servo4.write(pos);     // Set Servo 4 position to 'pos' degrees
  delay(10);   // Pause for 15 milliseconds to control the speed of servo movement
  }
}

/*
NOTE:
This code is written for standard servo motors. If you are using  360 degree continous rotation servo, 
the servo.write (pos) function behave differently than standard servo. It controls speed rather than position.
A value near 90 means no movement, 0 is full speed in one direction and  180 is full speed in other direction
 
*/

