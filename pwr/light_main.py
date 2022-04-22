import time
import sys
from light import LightCtrl

light = LightCtrl(24, True)
sensor_light = LightCtrl(25, True)

def parsing_cmd(cmd):
    if cmd.lower() == "on":
        light.on()
    elif cmd.lower() == "off":
        light.off()
    elif cmd.lower() == "toggle":
        light.toggle()
    if cmd.lower() == "son":
        sensor_light.on()
    elif cmd.lower() == "soff":
        sensor_light.off()
    elif cmd.lower() == "stoggle":
        sensor_light.toggle()
    elif cmd.lower() == "quit" or cmd.lower() == "exit":
        exit()
    else:
        print("Unknown Command")

def main():

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
