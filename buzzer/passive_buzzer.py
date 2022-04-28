import RPi.GPIO as GPIO
import sys
import time

pin_num = None

def buzzer_init(buzzer_pin_num = 18):
    global pin_num

    GPIO.setmode(GPIO.BCM)
    pin_num = buzzer_pin_num
    GPIO.setup(pin_num, GPIO.OUT)

def buzzer_on():
    if not pin_num:
        print("pin number not defined")
        return
    print("Buzzer On :", pin_num)
    buz = GPIO.PWM(pin_num, 20000)
    buz.start(50)

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
    buzzer_init(18)

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

    while True:
        time.sleep(0.1)

if __name__ == '__main__':
    main()
