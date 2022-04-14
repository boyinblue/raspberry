#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

pin_num = None

def serbo_init(serbo_pin_num = 18):
    global pin_num

    GPIO.setmode(GPIO.BCM)
    pin_num = serbo_pin_num
    GPIO.setup(pin_num, GPIO.OUT)

def set_degree(degree):
    phz = GPIO.PWM(pin_num, 100)
    phz.start(5)
    duty = degree / 10.0 + 2.5
    phz.ChangeDutyCycle(duty)
    time.sleep(0.5)

def main():
    while True:
        degree = float( input("제어할 각도 :") )
        set_degree(degree)

    GPIO.cleanup()

if __name__ == '__main__':
    serbo_init()
    main()
