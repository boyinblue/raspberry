#!/usr/bin/env python

import RPi.GPIO as GPIO

class Sensor:
    def __init__(self, pin_num, low_active=False):
        #GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        self.pin_num = pin_num
        self.low_active = low_active
        self.on_callback = None
        self.off_callback = None

        GPIO.setup(self.pin_num, GPIO.IN)
        self.cur = GPIO.input(self.pin_num)
        if self.low_active:
            self.cur = not self.cur
        self.prev = self.cur

    def __del__(self):
#        self.off()
        pass

    def regist_on_callback(self, func):
        self.on_callback = func

    def regist_off_callback(self, func):
        self.off_callback = func

    def sweep(self):
        self.cur = GPIO.input(self.pin_num)
        if self.low_active:
            self.cur = not self.cur

        if self.prev != self.cur:
            if self.cur and self.on_callback:
                self.on_callback()
            elif not self.cur and self.off_callback:
                self.off_callback()
            self.prev = self.cur

    def read(self):
        return self.cur
