import RPi.GPIO as GPIO

class LightCtrl:
    def __init__(self, light_pin_num, low_active=False):
        print("LightCtrl init({}, {})".format(light_pin_num, low_active))
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
        print("LightCtrl off()")
        if self.low_active:
            GPIO.output(self.pin_num, True)
        else:
            GPIO.output(self.pin_num, False)

    def on(self):
        print("LightCtrl on()")
        if self.low_active:
            GPIO.output(self.pin_num, False)
        else:
            GPIO.output(self.pin_num, True)

    def toggle(self):
        GPIO.output(self.pin_num, not GPIO.input(self.pin_num))
