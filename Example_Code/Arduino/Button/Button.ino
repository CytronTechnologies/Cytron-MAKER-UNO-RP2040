/*
DESCRIPTION:
This example code will show how to use the User button on the Maker Uno RP2040 as an Input.
In this code, the button will be used to control an on-board LED. 
If the button is pressed, the LED will light up for 0.5 second then turned off

AUTHOR  : Cytron Technologies Sdn Bhd
WEBSITE  : www.cytron.io
EMAIL    : support@cytron.io
*/

  // Declare pin assignments for LED and button. 
const int ledPin1 = 0;
const int btn1 = 2; 


void setup() {
  // initialize leds GP1 pins as output and the user button as output
  pinMode(ledPin1, OUTPUT);
  pinMode(btn1, INPUT_PULLUP);
  
}

void loop() {
  // check button 1 (GP2) is pressed
  if (!digitalRead(btn1)) {
    // led GP0 is light up for 0.5s then turned off.
    digitalWrite(ledPin1, HIGH);
    delay(500);
    digitalWrite(ledPin1, LOW);
  }

}
