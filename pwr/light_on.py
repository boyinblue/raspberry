import RPi.GPIO as GPIO

def light_on():
    #GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(15, GPIO.OUT)
    GPIO.output(15, False) #Low Active

if __name__ == '__main__':
    light_on()
