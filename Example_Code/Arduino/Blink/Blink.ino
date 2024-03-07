/*
DESCRIPTION:
This example code will use Maker Uno RP2040 to light up any of two onboard GPIOs LEDs alternately. 
For this code, GPIOs LED for GPO and GP1 pin are selected.
Each LED will be blinking every each 0.5 second alternately.  

AUTHOR   : Cytron Technologies Sdn Bhd
WEBSITE  : www.cytron.io
EMAIL    : support@cytron.io
*/

 // Pin assignments for LEDs
const int ledPin1 = 0;
const int ledPin2 = 1;

void setup() {
  // initialize leds on GP0 and GP1 pins as output.
  pinMode(ledPin1, OUTPUT);
  pinMode(ledPin2, OUTPUT);
}

void loop() {
  // led GP0 is light up for 0.5s then turned off.
  digitalWrite(ledPin1, HIGH);   
  delay(500);                      
  digitalWrite(ledPin1, LOW);  
  delay(500);                    

  // led GP1 is light up for 0.5s then turned off.
  digitalWrite(ledPin2, HIGH);  
  delay(500);      
  digitalWrite(ledPin2, LOW);  
  delay(500);                  
}
