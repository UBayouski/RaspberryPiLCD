#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import Adafruit_DHT

from RPLCD import CharLCD

GPIO.cleanup()
lcd = CharLCD(numbering_mode=GPIO.BOARD, cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[40, 38, 36, 32, 33, 31, 29, 23])

while True:

    humidity, temperature = Adafruit_DHT.read_retry(11, 18)

    print('Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity))
    lcd.clear()
    lcd.cursor_pos = (0, 0)
    lcd.write_string("Temp: %d C" % temperature)
    lcd.cursor_pos = (1, 0)
    lcd.write_string("Humidity: %d %%" % humidity)

    time.sleep(5)
