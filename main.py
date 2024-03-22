import smartlock
from smartlock import MySmartLock
from mqtt import MyMQTT
import machine
from machine import Pin
import time
from motor import MyMotor

d2=Pin(13,Pin.OUT)

a=0
while(a < 5):
    d2.value(1)
    time.sleep(0.2)
    d2.value(0)
    time.sleep(0.2)
    a = a + 1

#LimitSwitch1 = Pin(10,Pin.IN)
#LimitSwitch2 = Pin(6,Pin.IN)
#while True:
#    time.sleep(0.5)
#    print(LimitSwitch1.value(),LimitSwitch2.value())
    

#Motor = MyMotor(12,18,19)
#Motor.run("fan")
#time.sleep(2)
#Motor.run("ting")

#初始化智能锁
lock = MySmartLock(12,18,19)

#初始化mqtt联网，大约监听六十秒
mqtt = MyMQTT()
mqtt.initLock(lock)
mqtt.func_connect()

#让单片机休眠
#import sleep