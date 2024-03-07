/*
DESCRIPTION:
This example code will use the the buzzzer on the Maker Uno RP2040 to play the tones. 
The User button also used in this code. Upon startup, a short melody will be played 
and then the code will wait for the button press to play another set of short tones.

AUTHOR   : Cytron Technologies Sdn Bhd
WEBSITE  : www.cytron.io
EMAIL    : support@cytron.io
*/

// Declare pin assigment for buzzer and button
const int buzzerPin = 8;
const int btn1 = 2;

// Create an array of the melody note frequency with its corresponding duration for each note
int melody_note[10] = {659, 659, 0, 659, 0, 523, 659, 0, 784, 0}; // [E5, E5, REST, E5, REST, C5, E5, REST, G5]
int melody_duration[10] = {150, 150, 150, 150, 150, 150, 150, 150, 200, 150};

void setup(){

  // Initialize buzzer pin as output
  pinMode(buzzerPin, OUTPUT);

  // Initialize buttons
  pinMode(btn1, INPUT_PULLUP);

  // Play melody during start up
  play_melody(buzzerPin);
  
}

void loop(){

  // Check button 1 (GP2) is pressed
  if (!digitalRead(btn1)) {
    // Play tones
    tone(buzzerPin,262,100);
    delay(100);
    tone(buzzerPin,659,100);
    delay(100);
    tone(buzzerPin,784,100);
    delay(100);
    noTone(buzzerPin);
  }

  
}

void play_melody(int pin){
  for(int i=0; i<10; i++){
    if(melody_note[i] == 0){
      noTone(pin);
    } 
    else{
     tone(pin, melody_note[i], 100);
    }
    delay(int(melody_duration[i]));
  }
}

