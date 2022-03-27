import RPi.GPIO as GPIO
import sys
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

class SensorLight:
    def __init__(self, pin_num_sensor, pin_num_light, timer = 60):
        self.pin_num_sensor = pin_num_sensor
        self.pin_num_light = pin_num_light
        self.timer = timer
        self.time = 0

        GPIO.setup(pin_num_sensor, GPIO.IN)
        GPIO.setup(pin_num_light, GPIO.OUT)

        self.prev_sensor = GPIO.input(pin_num_sensor)
        self.sensor = GPIO.input(pin_num_sensor)

    def polling(self):
        self.sensor = GPIO.input(self.pin_num_sensor)
        if self.sensor:
            self.sensor_on()
        else:
            self.sensor_off()

    def sensor_on(self):
        if self.sensor != self.prev_sensor:
            self.sensor_on_event()
            self.prev_sensor = self.sensor

    def sensor_off(self):
        if self.sensor != self.prev_sensor:
            self.sensor_off_event()
            self.prev_sensor = self.sensor

    def sensor_on_event(self):
        GPIO.output(self.pin_num_light, True)

    def sensor_off_event(self):
        GPIO.output(self.pin_num_light, False)
    

def main():
    sensorlight = SensorLight(18, 22)
    while True:
        sensorlight.polling()
        time.sleep(0.1)

if __name__ == '__main__':
    main()
