import RPi.GPIO as GPIO

def pwr_on():
    #GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(14, GPIO.OUT)
    GPIO.output(14, False) #Low Active

if __name__ == '__main__':
    pwr_on()
