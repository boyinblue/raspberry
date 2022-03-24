import RPi.GPIO as GPIO
import sys

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)

def buzzer_on():
    GPIO.output(25, True)

def buzzer_off():
    GPIO.output(25, False)

def main():
    if sys.argv[1] == "on":
        buzzer_on()
    elif sys.argv[1] == "off":
        buzzer_off()

if __name__ == '__main__':
    main()
