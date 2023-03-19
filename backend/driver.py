from lcd import RgbLcd
from notification_lcd import NotificationLcd
from buzzer import Buzzer
from button import Button

import RPi.GPIO as GPIO

def cleanup():
    GPIO.cleanup()    