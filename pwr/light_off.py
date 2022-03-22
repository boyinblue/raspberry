import RPi.GPIO as GPIO

def light_off():
    #GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(24, GPIO.OUT)
    GPIO.output(24, True) #Low Active

if __name__ == '__main__':
    light_off()
