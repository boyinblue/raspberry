import RPi.GPIO as GPIO
import sys
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)

def stop():
    GPIO.output(26, False)
    GPIO.output(19, False)
    GPIO.output(13, False)
    GPIO.output(6, False)

def pre_run():
    GPIO.output(26, True)
    GPIO.output(19, False)
    GPIO.output(13, False)
    GPIO.output(6, False)
    time.sleep(0.05)

def run():
    cnt = 0
    while True:
        if cnt % 8 == 0:
            GPIO.output(26, True)
            GPIO.output(19, False)
            GPIO.output(13, False)
            GPIO.output(6, False)
        elif cnt % 8 == 1:
            GPIO.output(26, True)
            GPIO.output(19, True)
            GPIO.output(13, False)
            GPIO.output(6, False)
        elif cnt % 8 == 2:
            GPIO.output(26, False)
            GPIO.output(19, True)
            GPIO.output(13, False)
            GPIO.output(6, False)
        elif cnt % 8 == 3:
            GPIO.output(26, False)
            GPIO.output(19, True)
            GPIO.output(13, True)
            GPIO.output(6, False)
        elif cnt % 8 == 4:
            GPIO.output(26, False)
            GPIO.output(19, False)
            GPIO.output(13, True)
            GPIO.output(6, False)
        elif cnt % 8 == 5:
            GPIO.output(26, False)
            GPIO.output(19, False)
            GPIO.output(13, True)
            GPIO.output(6, True)
        elif cnt % 8 == 6:
            GPIO.output(26, False)
            GPIO.output(19, False)
            GPIO.output(13, False)
            GPIO.output(6, True)
        elif cnt % 8 == 7:
            GPIO.output(26, True)
            GPIO.output(19, False)
            GPIO.output(13, False)
            GPIO.output(6, True)
        cnt = cnt + 1
        time.sleep(0.0005)

def main():
    stop()
    pre_run()
    run()

if __name__ == '__main__':
    main()
