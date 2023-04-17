from machine import Pin, I2C
import dht
import ssd1306
import time

sens=dht.DHT11(Pin(12))
i2c=I2C(sda=Pin(4),scl=Pin(5))
display=ssd1306.SSD1306_I2C(128,64,i2c)


while True:
    display.fill(0)
    sens.measure()
    display.text("Weather Station",0,0,1)
    display.text("Celsius: "+str(sens.temperature())+"C",0,28,1)
    display.text("Humidity: "+str(sens.humidity())+"%RH",0,55,1)
    display.show()
    time.sleep(0.01)
