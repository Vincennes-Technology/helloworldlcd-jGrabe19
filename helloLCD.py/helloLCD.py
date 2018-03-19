#show IP address on the LCD Plate at startup
#

import Adafruit_CharLCD as LCD
import time
import subprocess

lcd = LCD.Adafruit_CharLCDPlate()

Name = subprocess.check_output(['hostname']).strip()
IPaddr = subprocess.check_output(['hostname', '-I'])
displayText = "Hello World\n"
displayText2 = IPaddr + Name
lcd.clear()
lcd.message(displayText)
Refresh = True
Wrefresh = True

while (True):
    if lcd.is_pressed(LCD.SELECT):
        if Wrefresh:
            lcd.set_backlight(1)
            lcd.clear()
            lcd.message(displayText)
            Refresh = True
            Wrefresh = False

    else:
        if Refresh:
            lcd.set_backlight(1)
            lcd.clear()
            lcd.message(displayText2)
            Refresh = False
            Wrefresh = True
    time.sleep(0.5)
