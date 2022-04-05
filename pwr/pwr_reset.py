import RPi.GPIO as GPIO
import time

def pwr_reset():
    #GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.OUT)
    GPIO.output(17, True) #Low Active

    time.sleep(15)

    GPIO.output(17, False) #Low Active

if __name__ == '__main__':
    pwr_reset()
