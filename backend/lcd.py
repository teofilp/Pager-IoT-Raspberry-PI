import time,sys


# this device has two I2C addresses
DISPLAY_RGB_ADDR = 0x62
DISPLAY_TEXT_ADDR = 0x3e
        
class RgbLcd:
    def __init__(self):
        self.bus = None
        self._setup()

    def _setup(self):
        if sys.platform == 'uwp':
            import winrt_smbus as smbus
            self.bus = smbus.SMBus(1)
        else:
            import smbus
            import RPi.GPIO as GPIO
            rev = GPIO.RPI_REVISION
            if rev == 2 or rev == 3:
                self.bus = smbus.SMBus(1)
            else:
                self.bus = smbus.SMBus(0)
    # set backlight to (R,G,B) (values from 0..255 for each)
    def setRGB(self, r,g,b):
        self.bus.write_byte_data(DISPLAY_RGB_ADDR,0,0)
        self.bus.write_byte_data(DISPLAY_RGB_ADDR,1,0)
        self.bus.write_byte_data(DISPLAY_RGB_ADDR,0x08,0xaa)
        self.bus.write_byte_data(DISPLAY_RGB_ADDR,4,r)
        self.bus.write_byte_data(DISPLAY_RGB_ADDR,3,g)
        self.bus.write_byte_data(DISPLAY_RGB_ADDR,2,b)

    # send command to display (no need for external use)    
    def textCommand(self, cmd):
        self.bus.write_byte_data(DISPLAY_TEXT_ADDR,0x80,cmd)

    # set display text \n for second line(or auto wrap)     
    def setText(self, text):
        self.textCommand(0x01) # clear display
        time.sleep(.05)
        self.textCommand(0x08 | 0x04) # display on, no cursor
        self.textCommand(0x28) # 2 lines
        time.sleep(.05)
        count = 0
        row = 0
        for c in text:
            if c == '\n' or count == 16:
                count = 0
                row += 1
                if row == 2:
                    break
                self.textCommand(0xc0)
                if c == '\n':
                    continue
            count += 1
            self.bus.write_byte_data(DISPLAY_TEXT_ADDR,0x40,ord(c))

    #Update the display without erasing the display
    def setText_norefresh(self, text):
        self.textCommand(0x02) # return home
        time.sleep(.05)
        self.textCommand(0x08 | 0x04) # display on, no cursor
        self.textCommand(0x28) # 2 lines
        time.sleep(.05)
        count = 0
        row = 0
        while len(text) < 32: #clears the rest of the screen
            text += ' '
        for c in text:
            if c == '\n' or count == 16:
                count = 0
                row += 1
                if row == 2:
                    break
                self.textCommand(0xc0)
                if c == '\n':
                    continue
            count += 1
            self.bus.write_byte_data(DISPLAY_TEXT_ADDR,0x40,ord(c))        
