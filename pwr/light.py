import RPi.GPIO as GPIO

class LightCtrl:
    def __init__(self, light_pin_num, low_active=False):
        #GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        self.pin_num = light_pin_num
        self.low_active = low_active
        GPIO.setup(self.pin_num, GPIO.OUT)
        self.off()

    def __del__(self):
#        self.off()
        pass

    def off(self):
        if self.low_active:
            GPIO.output(self.pin_num, True)
        else:
            GPIO.output(self.pin_num, False)

    def on(self):
        if self.low_active:
            GPIO.output(self.pin_num, False)
        else:
            GPIO.output(self.pin_num, True)

    def toggle(self):
        GPIO.output(self.pin_num, not GPIO.input(self.pin_num))
