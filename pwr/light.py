import RPi.GPIO as GPIO

class LightCtrl

def sensor_light_on():
    #GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(22, GPIO.OUT)
    GPIO.output(22, False) #Low Active

def light_on():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(27, GPIO.OUT)
    GPIO.output(27, False) #Low Active

if __name__ == '__main__':
    light_on()
