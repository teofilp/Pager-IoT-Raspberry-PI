import RPi.GPIO as GPIO
import time
import threading

BUZZER_PIN = 12

default_melody = [("C4", 0.25), ("D4", 0.25), ("E4", 0.25), ("F4", 0.25), ("G4", 0.25), ("B4", 0.25), ("C5", 0.5)]

class Buzzer:
    def __init__(self, pin = BUZZER_PIN, melody = default_melody):
        self.pin = pin
        self.melody = melody
        self.playing = False
        
        self._setup_device()

    def _setup_device(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT)

    def start_playing(self):
        self.playing = True
        threading.Thread(target=self._play_song).start()

    def stop_playing(self):
        self.playing = False

    def _play_song(self):
        while self.playing == True:
            for note, duration in self.melody:
                if self.playing == False:
                    break

                # Compute frequency of the note
                freq = 440 * 2 ** ((ord(note[0]) - ord("A")) / 12)
            
                #Turn the buzzer on at the frequency of the note
            
                GPIO.output(self.pin, GPIO.HIGH)
                buzzer = GPIO.PWM(self.pin, freq)
                buzzer.start(5)
            
                #Wait for the duration of the note
                time.sleep(duration)
            
                #Stop the buzzer and turn it off
                buzzer.stop()
                GPIO.output(self.pin, GPIO.LOW)
            
                #Wait for a short time before playing the next note
                time.sleep(0.1)
            time.sleep(1.5)
