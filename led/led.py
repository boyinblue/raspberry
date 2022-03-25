import RPi.GPIO as GPIO
import sys

led_r_pin = 21
led_g_pin = 20
led_b_pin = 16

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_r_pin, GPIO.OUT)
GPIO.setup(led_g_pin, GPIO.OUT)
GPIO.setup(led_b_pin, GPIO.OUT)

def led_r_on():
    GPIO.output(led_r_pin, True)

def led_r_off():
    GPIO.output(led_r_pin, False)

def led_g_on():
    GPIO.output(led_g_pin, True)

def led_g_off():
    GPIO.output(led_g_pin, False)

def led_b_on():
    GPIO.output(led_b_pin, True)

def led_b_off():
    GPIO.output(led_b_pin, False)

def is_led_r_on():
    return GPIO.input(led_r_pin)

def is_led_g_on():
    return GPIO.input(led_g_pin)

def is_lef_b_on():
    return GPIO.input(led_b_pin)

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
    pin_num = led_r_pin

    if sys.argv[1] == "r":
        pin_num = led_r_pin
    elif sys.argv[1] == "g":
        pin_num = led_g_pin
    elif sys.argv[1] == 'b':
        pin_num = led_b_pin

    if sys.argv[2] == "on":
        GPIO.output(pin_num, True)
    else:
        GPIO.output(pin_num, False)

if __name__ == '__main__':
    main()
