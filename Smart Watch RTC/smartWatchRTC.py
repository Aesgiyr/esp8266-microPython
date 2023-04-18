from machine import Pin, I2C, RTC
import dht
import ssd1306
import time

sens=dht.DHT11(Pin(12))
rtc = RTC()
i2c=I2C(sda=Pin(4),scl=Pin(5))
display=ssd1306.SSD1306_I2C(128,64,i2c)

while True:
    display.fill(0)
    sens.measure()
    display.text(str(sens.temperature())+"C",100,0,1)
    display.text(str(sens.humidity())+"%RH",85,10,1)
    display.text("Year: "+str(rtc.datetime()[0]),0,0,1)
    display.text("Month: "+str(rtc.datetime()[1]),0,10,1)
    display.text("Day: "+str(rtc.datetime()[2]),0,20,1)
    display.text("Hour: "+str(rtc.datetime()[4]),0,30,1)
    display.text("Minute: "+str(rtc.datetime()[5]),0,40,1)
    display.text("Second: "+str(rtc.datetime()[6]),0,50,1)
    display.show()
    time.sleep(0.01)