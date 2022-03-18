import sys

sys.path.append("../pwr")
sys.path.append("../led")

import light_on
import light_off
import led

import RPi.GPIO as GPIO
import time
import atexit

cnt = 0
state = 0

def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.IN)
    atexit.register(exit_handler)

def exit_handler():
    light_off.light_off()

def sensor_turn_on():
    global cnt
    global state

    cnt = 0
    state = 1
    light_on.light_on()

def sensor_on():
    led.led_r_toggle()

def sensor_off():
    global state
    global cnt

    if state != 0:
#        print(cnt)
        cnt += 0.1
        if cnt > 300:
#        if cnt > 5:
            light_off.light_off()
            cnt = 0
            state = 0

def main():
    value_prev = 0
    while True:
        value = GPIO.input(18)
        if value != value_prev:
            value_prev = value
            if value == 1:
                sensor_turn_on()

        if value == 0:
            sensor_off()
        else:
            sensor_on()
            
        time.sleep(0.1)

if __name__ == '__main__':
    init()
    main()
