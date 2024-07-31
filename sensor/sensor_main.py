#!/usr/bin/env python

from sensor import Sensor
import time

ir_sensor = Sensor(18)

def sensor_on():
    print("센서 켜짐")

def sensor_off():
    print("센서 꺼짐")

ir_sensor.regist_on_callback(sensor_on)
ir_sensor.regist_off_callback(sensor_off)

while True:
    ir_sensor.sweep()
    time.sleep(0.1)
