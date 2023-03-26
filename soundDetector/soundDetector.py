from machine import ADC, Pin
import time

ledR=Pin(0,Pin.OUT,value=0)
ledG=Pin(4,Pin.OUT,value=0)
adc = ADC(0)

while True:
    
    print(adc.read())
    readValue = adc.read()
    
    if readValue<57:
        ledG.off()
        ledR.on()
        time.sleep(0.5)
    elif readValue>=57:
        ledR.off()
        ledG.on()