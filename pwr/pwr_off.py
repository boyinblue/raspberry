import RPi.GPIO as GPIO

def pwr_off():
    #GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(12, GPIO.OUT)
    GPIO.output(12, True) #Low Active

if __name__ == '__main__':
    pwr_off()
