import RPi.GPIO as GPIO

def pwr_off():
    #GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(14, GPIO.OUT)
    GPIO.output(14, True) #Low Active

if __name__ == '__main__':
    pwr_off()
