/*
DESCRIPTION:
This example code will demonstrate how to use Maker UNO RP2040 with OLED Display SSD1315 to display text.

CONNECTION:
Grove 6 of Maker UNO RP2040 - OLED Display SSD1315 Grove

GP20 - SDA
GP21 - SCL

AUTHOR   : Cytron Technologies Sdn Bhd
WEBSITE  : www.cytron.io
EMAIL    : support@cytron.io

REFERENCE:
Code adapted from:
https://wiki.seeedstudio.com/Grove-OLED-Display-0.96-SSD1315/
*/
#include <Arduino.h>
#include <U8g2lib.h>
#ifdef U8X8_HAVE_HW_SPI
#include <SPI.h>
#endif
#ifdef U8X8_HAVE_HW_I2C
#include <Wire.h>
#endif

U8G2_SSD1306_128X64_NONAME_F_SW_I2C u8g2(U8G2_R0, /* clock(SCL)*/ SCL, /*data(SDA)*/ SDA, /* reset=*/ U8X8_PIN_NONE);

void setup(void) {
  u8g2.begin();
}

void loop(void) {
  u8g2.clearBuffer();
  u8g2.setFont(u8g2_font_ncenB08_tr);

  // Adjusted coordinates for better positioning
  u8g2.drawStr(5, 15, "Hello World!");
  u8g2.drawStr(5, 30, "Yeah!");

  u8g2.sendBuffer();
  delay(1000);
}
