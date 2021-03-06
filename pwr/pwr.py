import RPi.GPIO as GPIO
import time

pin_num = None

def pwr_init(pwr_pin_num=12):
    global pin_num

    pin_num = pwr_pin_num
    #GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin_num, GPIO.OUT)

def pwr_on():
    GPIO.output(pin_num, False) #Low Active

def pwr_off():
    GPIO.output(pin_num, True) #Low Active

def pwr_reset():
    if GPIO.input(pin_num) == 0:
        print("Pwr Off For 15 secs")
        pwr_off()
        time.sleep(15)
    print("Pwr On")
    pwr_on()

if __name__ == '__main__':
    pwr_init()
    pwr_reset()
