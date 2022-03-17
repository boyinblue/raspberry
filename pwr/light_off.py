import RPi.GPIO as GPIO

def light_off():
    #GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(15, GPIO.OUT)
    GPIO.output(15, True) #Low Active

if __name__ == '__main__':
    light_off()
