import threading
import time

import driver

class NotificationService:
    def __init__(self):        
        self.read = False
        self.message = ""
        
        self.lcd = driver.NotificationLcd()
        self.buzzer = driver.Buzzer()
        self.button = driver.Button()
        self.button.add_click_listener(self.read_notification)

    def add_notification(self, new_message):
        self.message = new_message
        self.read = False        
        self.buzzer.start_playing()
        self.lcd.show_pending_notification()
        
    def read_notification(self, channel):
        if self.read == False:
            self.buzzer.stop_playing()
            self.lcd.show_notification(self.message)
        
        self.read = True
        
    def cleanup(self):
        driver.cleanup()
