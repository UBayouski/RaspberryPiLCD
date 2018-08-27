#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import Adafruit_DHT

from RPLCD import CharLCD

# We call a RPi.GPIO built-in function GPIO.cleanup() to clean up all the ports we've used
GPIO.cleanup()

# Now setup LCD display pins (8-bit mode)
lcd = CharLCD(numbering_mode=GPIO.BOARD, cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[40, 38, 36, 32, 33, 31, 29, 23])

# Get senosr readings and render them in a loop
while True:

    # Get sensor's readings
    # IMPORTANT: 11 is sensor type (DHT11) and 18 is GPIO number (or physical pin 12)
    humidity, temperature = Adafruit_DHT.read_retry(11, 18)

    print('Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity))

    # Clear and set initial cursor position for LCD display
    lcd.clear()
    lcd.cursor_pos = (0, 0)

    # Render temperature readings
    lcd.write_string("Temp: %d C" % temperature)

    #  Move cursor to second row
    lcd.cursor_pos = (1, 0)

    # Render humidity readings
    lcd.write_string("Humidity: %d %%" % humidity)

    # Pause execution for 5 seconds
    time.sleep(5)
