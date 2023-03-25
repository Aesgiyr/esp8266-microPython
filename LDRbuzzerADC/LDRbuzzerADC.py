from machine import ADC, Pin, PWM
import time

led=Pin(0,Pin.OUT,value=0)
adc = ADC(0)

while True:
    
    print(adc.read())
    time.sleep(0.1)
    readValue = adc.read()
    
    if readValue<950:
        beep=PWM(Pin(4),freq=294,duty=600)
        led.on()
        time.sleep(0.2)
        beep.deinit()
    else:
        led.off()
        