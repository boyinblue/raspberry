import RPi.GPIO as GPIO

def sensor_light_off():
    #GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(22, GPIO.OUT)
    GPIO.output(22, True) #Low Active

def light_off():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(27, GPIO.OUT)
    GPIO.output(27, True) #Low Active

if __name__ == '__main__':
    light_off()
