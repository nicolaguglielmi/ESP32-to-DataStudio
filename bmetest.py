#A quick POW to check that the board get the values from the sensors
import machine
#from machine import Pin, ADC, I2C,RTC
from third_party import BME280
import time

# ESP32 - Pin assignment
i2c = machine.I2C(scl=machine.Pin(22), sda=machine.Pin(21), freq=10000)

while True:
    bme = BME280.BME280(i2c=i2c)
    temp = bme.temperature
    humi = bme.humidity
    pres = bme.pressure
    print("_____________________")
    print("Temperature :",temp)
    print("Humidity    :",humi)
    print("Pressure    :",pres)
    print("_____________________")
    time.sleep(10)
