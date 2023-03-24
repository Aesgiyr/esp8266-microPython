from machine import ADC, Pin
import time

ledLeft=Pin(0,Pin.OUT,value=0)
ledMid=Pin(4,Pin.OUT,value=0)
ledRight=Pin(5,Pin.OUT,value=0)
ledLeftM=Pin(1,Pin.OUT,value=0)
ledRightM=Pin(3,Pin.OUT,value=0)
adc = ADC(0)

while True:
    print(adc.read())
    readValue = adc.read()
    
    if readValue<540 and readValue>520:
        ledMid.on()
        time.sleep(0.1)
        ledMid.off()
        time.sleep(0.1)
        
    elif readValue<100:
        ledLeft.on()
        time.sleep(0.1)
        ledLeft.off()
        time.sleep(0.1)
        
    elif readValue<500:
        ledLeftM.on()
        time.sleep(0.1)
        ledLeftM.off()
        time.sleep(0.1)
        
    elif readValue>950:
        ledRight.on()
        time.sleep(0.1)
        ledRight.off()
        time.sleep(0.1)
        
    elif readValue>545:
        ledRightM.on()
        time.sleep(0.1)
        ledRightM.off()
        time.sleep(0.1)
        
    
