#!/bin/usr/env python

import RPi.GPIO as GPIO
import sys

led_pin = {'r':21, 'g':20, 'b':16}

def led_init(r=21, g=20, b=16):
    global led_pin

    led_pin['r'] = r
    led_pin['g'] = g
    led_pin['b'] = b

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    for pin in led_pin.values():
        print("Set output :", pin)
        GPIO.setup(pin, GPIO.OUT)

def led_r_on():
    GPIO.output(led_pin['r'], True)

def led_r_off():
    GPIO.output(led_pin['r'], False)

def led_g_on():
    GPIO.output(led_pin['g'], True)

def led_g_off():
    GPIO.output(led_pin['g'], False)

def led_b_on():
    GPIO.output(led_pin['b'], True)

def led_b_off():
    GPIO.output(led_pin['b'], False)

def led_all_off():
    led_r_off()
    led_g_off()
    led_b_off()

def is_led_r_on():
    return GPIO.input(led_pin['r'])

def is_led_g_on():
    return GPIO.input(led_pin['g'])

def is_led_b_on():
    return GPIO.input(led_pin['b'])

def led_r_toggle():
    if is_led_r_on():
        led_r_off()
    else:
        led_r_on()

def led_g_toggle():
    if is_led_g_on():
        led_g_off()
    else:
        led_g_on()

def led_b_toggle():
    if is_led_b_on():
        led_b_off()
    else:
        led_b_on()

def print_usage():
    print("(Usage) {} (led pin) (ctrl)".format(sys.argv[0]))
    print("(Example) {} r on".format(sys.argv[0]))

def main():
    if len(sys.argv) < 2:
        print("Please select pin")
        print_usage()
        return

    pin_num = None
    if sys.argv[1] == "r":
        pin_num = led_pin['r']
    elif sys.argv[1] == "g":
        pin_num = led_pin['g']
    elif sys.argv[1] == 'b':
        pin_num = led_pin['b']
    else:
        print("Unknown pin :", sys.argv[1])
        return

    if sys.argv[2] == "on":
        GPIO.output(pin_num, True)
    else:
        GPIO.output(pin_num, False)

if __name__ == '__main__':
    led_init()
    main()
