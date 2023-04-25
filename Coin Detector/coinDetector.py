from machine import Pin, PWM, ADC
import time

pin = Pin(5,Pin.IN)
ledB=Pin(16,Pin.OUT,value=0)

while True:
    value = pin.value()
    print(pin.value())
    time.sleep(0.01)
    
    if value==1:
        ledB.on()
        beep=PWM(Pin(4),freq=220,duty=512)
    else:
        ledB.off()
        beep=PWM(Pin(4),freq=220,duty=512)
        beep.deinit()
        
        