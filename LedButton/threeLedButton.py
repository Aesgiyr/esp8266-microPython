from machine import Pin
import time

ledB=Pin(4,Pin.OUT,value=0)
ledG=Pin(0,Pin.OUT,value=0)
ledR=Pin(5,Pin.OUT,value=0)
button =Pin(12, Pin.IN, Pin.PULL_UP)
i=0
while True:
    if not button():
        i+=1
    if i==1:
        ledR.on()
        time.sleep(0.1)
        ledR.off()
        time.sleep(0.1)
    elif i==2:
        ledB.on()
        time.sleep(0.1)
        ledB.off() 
        time.sleep(0.1)
    elif i==3:
        ledG.on()
        time.sleep(0.1)
        ledG.off()
        time.sleep(0.1)
    elif i==4:
        i=0
    elif button():
        pass

    
    
        
