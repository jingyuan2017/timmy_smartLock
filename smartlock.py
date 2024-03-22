from motor import MyMotor
import machine
from machine import Pin
import time

class MySmartLock:

    def __init__(self,in1,in2,pwm):
        
        self.Motor = MyMotor(in1,in2,pwm)
        self.LimitSwitch1 = Pin(10,Pin.IN,Pin.PULL_UP)
        self.LimitSwitch2 = Pin(6,Pin.IN,Pin.PULL_UP)
        self.a=Pin(7,Pin.OUT)
        self.a1=Pin(11,Pin.OUT)
        
    #这里是收到开锁指令后的入口点     
    def openLock(self):
        print("我要开锁了啊")        
        self.Motor.run("zheng")
        
        self.a.value(1)
        self.a1.value(0)
        print("电机开始正转")
        while True:
            time.sleep(0.1)
            print(self.LimitSwitch1.value(),self.LimitSwitch2.value())
            if self.LimitSwitch1.value() == 0:
                self.Motor.run("ting")
                self.a.value(0)
                self.a1.value(0)
                print("电机停转")
                self.Motor.run("fan")
                #time.sleep(3)
                print("电机开始反转")
                self.a.value(0)
                self.a1.value(1)
                break
#             else:
#                 print(" ")
                
        while True:
            time.sleep(0.1)
            print(self.LimitSwitch1.value(),self.LimitSwitch2.value(),0)
            if self.LimitSwitch2.value() == 0:
                self.Motor.run("ting")
                self.a.value(0)
                self.a1.value(0)
                print("开锁成功")
                self.Motor.run("zheng")
                time.sleep(0.5)
                self.Motor.run("ting")
                break
            
