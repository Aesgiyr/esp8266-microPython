from machine import Pin, PWM, ADC
import time

ledB=Pin(0,Pin.OUT,value=0)
adc = ADC(0)

while True:
    print(adc.read())
    time.sleep(0.1)
    readValue = adc.read()
    if readValue!=1024:
        ledB.off()
        beep=PWM(Pin(4),freq=440,duty=512)
        beep.deinit()
    else: 
        ledB.on()
        beep=PWM(Pin(4),freq=200,duty=512)
    