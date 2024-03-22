import machine
from machine import Pin
import time

class MyMotor:
    def __init__(self,in1,in2,pwm):
        
        #接收初始化参数
        self.in1=in1
        self.in2=in2
        self.pwm=pwm
        
        #初始化引脚
        self.pinIn1 = Pin(self.in1,Pin.OUT)
        self.pinIn2 = Pin(self.in2,Pin.OUT)
        self.pinPwm = machine.PWM(Pin(self.pwm), freq=50)
        
        
        #初始化运行参数
        self.pinPwm.duty(500)
        self.pinIn1.value(0)
        self.pinIn2.value(0)
        
    def run(self,command):
        if command=="zheng":
            self.pinIn1.value(1)
            self.pinIn2.value(0)
        elif command=="fan":
            self.pinIn1.value(0)
            self.pinIn2.value(1)            
        elif command=="ting":
            self.pinIn1.value(0)
            self.pinIn2.value(0)
#a=MyMotor(1,2,40)
#a.run("zheng")
