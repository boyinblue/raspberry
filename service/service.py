import sys
import os

sys.path.append("../pwr")
sys.path.append("../led")
sys.path.append("../buzzer")
sys.path.append("../ir_recv")

import light
import led
import buzzer
import pyirw

import RPi.GPIO as GPIO
import time
import atexit

pipe_path = "/tmp/mypipe"

cnt_for_off = 0
state = {"sensor":0}
sensor_option = True
value_prev = {
    "sensor":False,
    "sw3":True,
    "sw4":True }
value_cur = {
    "sensor":False,
    "sw3":False,
    "sw4":False }
pin_nums = {
    "sensor":18,
    "sw3":4,
    "sw4":5,
    "buzzer":25}

def init():
    GPIO.setmode(GPIO.BCM)
    for pin_num in pin_nums.values():
        GPIO.setup(pin_num, GPIO.IN)
    atexit.register(exit_handler)

    light.light_init()
    light.light_off()
    light.sensor_light_off()
    buzzer.buzzer_init(pin_nums['buzzer'])

    led.led_all_off()

    pyirw.init_irw(blocking = False)

def exit_handler():
    light.light_off()
    light.sensor_light_off()

def sensor_turn_on():
    global cnt_for_off
    global state
    global sensor_option

    if sensor_option == False:
        print("Do not turn on light")
        return

    cnt_for_off = 0
    state['sensor'] = 1
    light.sensor_light_on()
    print("Sensor Light Turn On")

def sensor_turn_off():
    pass

def sensor_on():
    pass
#    buzzer.buzzer_on()

def handle_sensor_light():
    global state
    global cnt_for_off
    global sensor_option

#    buzzer.buzzer_off()
    if sensor_option == False:
        light.sensor_light_off()
        cnt_for_off = 0
        state['sensor'] = 0
        return

    if state['sensor'] != 0:
#        print(cnt)
        cnt_for_off += 0.1
        if cnt_for_off > 60:
#        if cnt > 5:
            light.sensor_light_off()
            cnt_for_off = 0
            state['sensor'] = 0

def set_sensor_option(option):
    global sensor_option

    if sensor_option != option:
        sensor_option = option
        print("Set Sensor Option :", sensor_option)

        if not sensor_option:
            light.sensor_light_off()
        elif value_prev['sensor']:
            light.sensor_light_on()
            state['sensor'] = 1

def toggle_sensor_option():
    set_sensor_option(not sensor_option)

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
            light.light_off()
        elif message[:13] == "Turn On Light":
            light.light_on()
        elif message[:13] == "Sensor Enable":
            set_sensor_option(True)
        elif message[:14] == "Sensor Disable":
            set_sensor_option(False)

def handle_sensor():
    value_cur['sensor'] = GPIO.input(pin_nums['sensor'])
    if value_cur['sensor'] != value_prev['sensor']:
        value_prev['sensor'] = value_cur['sensor']

    if value_cur['sensor'] == 0:
        sensor_off()
    else:
        sensor_on()

def handle_input():
    for key in value_cur.keys():
        value_cur[key] = GPIO.input(pin_nums[key])
        if value_cur[key] != value_prev[key]:
            print("{} changes {}".format(key, value_cur[key]))
            value_prev[key] = value_cur[key]
            if key == 'sw4' and value_cur[key] == False:
                toggle_sensor_option()
            elif key == 'sw3' and value_cur[key] == False:
                print("toggle light")
                light.light_toggle()
            elif key == 'sensor' and value_cur[key] == True:
                sensor_turn_on()

def handle_ir_recv():
    keyname, updown = pyirw.read_key()
    if keyname != '' and updown != '':
        keyname = keyname.decode('utf-8')
        updown = updown.decode('utf-8')
        print('%s (%s)' % (keyname, updown))
        
        if updown != '00':
            return

        if keyname == "KEY_RED":
            set_led_manual()
            led.led_r_toggle()
        elif keyname == "KEY_GREEN":
            set_led_manual()
            led.led_g_toggle()
        elif keyname == "KEY_BLUE":
            set_led_manual()
            led.led_b_toggle()

        buzzer.buzzer_beep(0.01)

def set_led_manual():
    if handle_led.manual == False:
        led.led_all_off()
        handle_led.manual = True
    handle_led.manual_cnt = 0

def handle_led():
    if handle_led.manual:
        handle_led.manual_cnt += 0.1
        if handle_led.manual_cnt > 10:
            handle_led.manual_cnt = 0
            handle_led.manual = False
            led.led_all_off()
        else:
            return

    if value_cur['sensor'] == True:
        led.led_all_off()
        led.led_r_on()
        handle_led.run_cnt = 0
        return
    else:
        led.led_r_off()

    handle_led.run_cnt += 0.1
    if handle_led.run_cnt >= 1:
        led.led_g_toggle()
        handle_led.run_cnt = 0

handle_led.run_cnt = 0
handle_led.manual = False
handle_led.manual_cnt = 0

def main():
    run_cnt = 0
    pipe = open_pipe()

    while True:
        handle_pipe(pipe)
        handle_input()
        handle_ir_recv()
        handle_led()
        handle_sensor_light()
        time.sleep(0.1)

if __name__ == '__main__':
    init()
    main()
