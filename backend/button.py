import RPi.GPIO as GPIO
import time

DEFAULT_BUTTON_PIN = 7

class Button:
    def __init__(self, pin = DEFAULT_BUTTON_PIN):
        self.button_pin = pin
        self._setup_device()
        
    def add_click_listener(self, callback):
        GPIO.add_event_detect(self.button_pin, GPIO.FALLING, callback=callback, bouncetime=150)
    
    def _setup_device(self):
        GPIO.setmode(GPIO.BOARD)    
        GPIO.setup(self.button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)        