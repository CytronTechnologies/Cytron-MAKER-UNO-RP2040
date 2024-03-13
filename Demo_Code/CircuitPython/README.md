# Demo Code for Maker Uno RP2040 

This demo code serve as an easy quality check when you receive this board. It is written in CircuitPython.

* **On startup**
  * Blue GPIO LEDs will light up in a countdown pattern.
  * A short melody starts playing, accompanied by the RGB LEDs alternating between blue and yellow, and the servo motor sweeping to 180 degrees.
  * The program will enter condition 0 and checking the push button's state.
  * Each button press will trigger different action.
  * The GPIO LEDs of GP20 and GP21 will act as condition LEDs. For example, when program in condition 1, GP20 LED will light up.

* **Condition 0 / No button press (Repeated loop)**
  * One half (upper half) of the Blue LEDs will light up from top to bottom while the other half (lower half) from bottom to top. (One LED will light up at a time for each half)
  * When the LEDs from both halves meet in the middle, the RGB LEDs will light up in a random color and remain lit until the next loop.
  * Simultaneously, the servo will sweep from 50 degrees to 0 degrees repeatedly.
    
* **Condition 1 / First Button Press**
  * GP20 LED lights up.
  * Buzzer will play notes in an ascending order.
  * Each note corresponds to a different number of LEDs light up, RGB LEDs' colour and the Servo position.
  * The higher the note, the more LEDs light up, and the greater the angles of the Servo motor.
  * For the RGB LEDs, the color changes from green to yellow to red as the note increases.

* **Condition 2 / Second Button Press**
  * GP20 LED turns off and GP21 LED lights up.
  * The same actions will be triggered as in Condition 1 but in reverse (descending note).
  * Program will reset to condition 0.
