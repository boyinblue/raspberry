#!/usr/bin/env python

import RPi.GPIO as GPIO
import sys
import time

pin_num = None

def buzzer_init(buzzer_pin_num = 13):
    global pin_num

    pin_num = buzzer_pin_num

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin_num, GPIO.OUT)
    GPIO.output(pin_num, False)

def buzzer_on():
    if not pin_num:
        print("pin number not defined")
        return
    GPIO.output(pin_num, True)

def buzzer_off():
    if not pin_num:
        print("pin number not defined")
        return
    GPIO.output(pin_num, False)

def buzzer_beep(duration=0.1, times=1):
    if not pin_num:
        print("pin number not defined")
        return
    for i in range(int(times)):
        buzzer_on()
        time.sleep(float(duration))
        buzzer_off()
        time.sleep(float(duration))

def main():
    buzzer_init()

    if sys.argv[1] == "on":
        buzzer_on()
    elif sys.argv[1] == "off":
        buzzer_off()
    elif sys.argv[1] == "beep":
        if len(sys.argv) > 3:
            buzzer_beep(sys.argv[2], sys.argv[3])
        elif len(sys.argv) > 2:
            buzzer_beep(sys.argv[2])
        else:
            buzzer_beep()

if __name__ == '__main__':
    main()
