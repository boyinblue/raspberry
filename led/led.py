import RPi.GPIO as GPIO
import sys

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

def led_r_on():
    GPIO.output(16, True)

def led_r_off():
    GPIO.output(16, False)

def led_g_on():
    GPIO.output(20, True)

def led_g_off():
    GPIO.output(20, False)

def led_b_on():
    GPIO.output(21, True)

def led_b_off():
    GPIO.output(21, False)

def is_led_r_on():
    return GPIO.input(16)

def is_led_g_on():
    return GPIO.input(20)

def is_lef_b_on():
    return GPIO.input(21)

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

def main():
    pin_num = 16


    if sys.argv[1] == "r":
        pin_num = 16
    elif sys.argv[1] == "g":
        pin_num = 20
    elif sys.argv[1] == 'b':
        pin_num = 21

    if sys.argv[2] == "on":
        GPIO.output(pin_num, True)
    else:
        GPIO.output(pin_num, False)

if __name__ == '__main__':
    main()
