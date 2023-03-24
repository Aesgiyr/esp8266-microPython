from machine import Pin, PWM
import time

led=Pin(5,Pin.OUT,value=0)
button =Pin(12, Pin.IN, Pin.PULL_UP)

while True:
    if not button():
        beep=PWM(Pin(4),freq=440,duty=512)
        led.on()
        time.sleep(0.1)
        led.off()
        beep.deinit()
    elif button():
        pass