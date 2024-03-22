import machine
from machine import Pin, deepsleep
import esp32
#pin = Pin(10, Pin.IN, Pin.PULL_UP)
#esp32.wake_on_ext0(pin, level = esp32.WAKEUP_ANY_HIGH)

pd = Pin(2, Pin.IN)
esp32.wake_on_ext0(pd,esp32.WAKEUP_ANY_HIGH)


btn1 = Pin(4, Pin.IN, Pin.PULL_UP)
esp32.wake_on_ext1(pins = (btn1, ), level = esp32.WAKEUP_ALL_LOW)

machine.deepsleep(20000)