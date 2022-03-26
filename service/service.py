import sys
import os

sys.path.append("../pwr")
sys.path.append("../led")
sys.path.append("../buzzer")

import light_on
import light_off
import led
import buzzer

import RPi.GPIO as GPIO
import time
import atexit

pipe_path = "/tmp/mypipe"

cnt_for_off = 0
state = 0
sensor_option = True

def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.IN)
    atexit.register(exit_handler)

    light_off.light_off()
    light_off.sensor_light_off()
    buzzer.buzzer_off()

    led.led_r_off()
    led.led_g_off()
    led.led_b_off()

def exit_handler():
    light_off.light_off()
    light_off.sensor_light_off()

def sensor_turn_on():
    global cnt_for_off
    global state
    global sensor_option

    if sensor_option == False:
        print("Do not turn on light")
        return

    cnt_for_off = 0
    state = 1
    light_on.sensor_light_on()

def sensor_turn_off():
    if sensor_option == False:
        return

def sensor_on():
    led.led_r_toggle()
#    buzzer.buzzer_on()

def sensor_off():
    global state
    global cnt_for_off
    global sensor_option

#    buzzer.buzzer_off()
    if sensor_option == False:
        cnt_for_off = 0
        state = 0
        return

    if state != 0:
#        print(cnt)
        cnt_for_off += 0.1
        if cnt_for_off > 60:
#        if cnt > 5:
            light_off.sensor_light_off()
            cnt_for_off = 0
            state = 0

def open_pipe():
    if not os.path.exists(pipe_path):
        os.mkfifo(pipe_path)
    os.chmod(pipe_path, 0o666)
    pipe_fd = os.open(pipe_path, os.O_RDONLY | os.O_NONBLOCK)
    return os.fdopen(pipe_fd)

def handle_pipe(pipe):
    global sensor_option

    message = pipe.readline()
    if message:
        print("Received : ", message)

        if message[:14] == "Turn Off Light":
            light_off.light_off()
        elif message[:13] == "Turn On Light":
            light_on.light_on()
        elif message[:13] == "Sensor Enable":
            sensor_option = True
        elif message[:14] == "Sensor Disable":
            sensor_option = False

def main():
    value_prev = 0
    run_cnt = 0
    pipe = open_pipe()

    while True:
        handle_pipe(pipe)

        value = GPIO.input(18)
        if value != value_prev:
            value_prev = value
            if value == 1:
                sensor_turn_on()
            else:
                sensor_turn_off()

        if value == 0:
            sensor_off()
        else:
            sensor_on()

        run_cnt = run_cnt + 0.1
        if run_cnt >= 1:
            led.led_g_toggle()
            run_cnt = 0
            
        time.sleep(0.1)

if __name__ == '__main__':
    init()
    main()
