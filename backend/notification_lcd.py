from lcd import RgbLcd
import threading
import time

class NotificationLcd(RgbLcd):
    def __init__(self):
        super().__init__()
        
    def show_pending_notification(self):
        self.setRGB(0, 255, 0)
        self.setText("Pending notification...")

    def show_notification(self, notification): 
        self.setRGB(0, 0, 255)
        self.setText(notification)

