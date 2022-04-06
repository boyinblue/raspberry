import RPi.GPIO as GPIO
import time
import sys

#class LightCtrl

def light_init():
    #GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(27, GPIO.OUT)
    GPIO.output(27, True) #Low Active
    GPIO.setup(22, GPIO.OUT)
    GPIO.output(22, True) #Low Active

def light_on():
    GPIO.output(27, False) #Low Active

def light_off():
    GPIO.output(27, True) #Low Active

def sensor_light_on():
    GPIO.output(22, False) #Low Active

def sensor_light_off():
    GPIO.output(22, True) #Low Active

def light_toggle():
    if GPIO.input(27) == True:
        GPIO.output(27, False)
    else:
        GPIO.output(27, True)

def parsing_cmd(cmd):
    if cmd.lower() == "on":
        light_on()
    elif cmd.lower() == "off":
        light_off()
    elif cmd.lower() == "toggle":
        light_toggle()
    elif cmd.lower() == "quit" or cmd.lower() == "exit":
        exit()
    else:
        print("Unknown Command")

def main():
    light_init()

    for i in range(1, len(sys.argv)):
        print("[ARG{}] {}".format(i, sys.argv[i]))

    if len(sys.argv) >= 2:
        parsing_cmd(sys.argv[1])
        return

    while True:
        cmd = input("cmd : ")
        parsing_cmd(cmd)

if __name__ == '__main__':
    main()
