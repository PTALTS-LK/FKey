#项目主页github.com/PCX-LK/FKey
#Powered by PCX-LK
#V1.1
from machine import UART,Pin
import time

uart = UART(2, baudrate=9600, tx=17, rx=16)#初始化uart通信
sw1 = Pin(32, Pin.IN, Pin.PULL_UP)#初始化引脚
sw2 = Pin(33, Pin.IN, Pin.PULL_UP)
sw3 = Pin(25, Pin.IN, Pin.PULL_UP)
sw4 = Pin(26, Pin.IN, Pin.PULL_UP)
bk = Pin(27, Pin.IN, Pin.PULL_UP)
l = Pin(2, Pin.OUT)#初始化LED发包指示灯

k1s = k2s = k3s = k4s = 0x00#预定义变量
k1ms = k2ms = k3ms = k4ms = 0
kso = [k1s,k2s,k3s,k4s]

#4个键的默认键码（默认dfjk），可自行更改，参见Docs/CH9329串口通信协议->附录1 “CH9329键码表”（HID Code）
k1def = 0x07
k2def = 0x09
k3def = 0x0d
k4def = 0x0e

while a == 0 :
    if bk.value() == 0 :#D27引脚中断程序
        break
    if sw1.value() == 0 :#按键检测
        k1 = chr(k1def)
        k1s = k1def
        k1ms = time.ticks_ms()
    elif time.ticks_diff(time.ticks_ms(), k1ms) >= 5 :
        k1 = b'\x00'
        k1s = 0x00

    if sw2.value() == 0 :
        k2 = chr(k2def)
        k2s = k2def
        k2ms = time.ticks_ms()
    elif time.ticks_diff(time.ticks_ms(), k2ms) >= 5 :
        k2 = b'\x00'
        k2s = 0x00

    if sw3.value() == 0 :
        k3 = chr(k3def)
        k3s = k3def
        k3ms = time.ticks_ms() 
    elif time.ticks_diff(time.ticks_ms(), k3ms) >= 5 :
        k3 = b'\x00'
        k3s = 0x00
    
    if sw4.value() == 0 :
        k4 = chr(k4def)
        k4s = k4def
        k4ms = time.ticks_ms()
    elif time.ticks_diff(time.ticks_ms(), k4ms) >= 5 :
        k4 = b'\x00'
        k4s = 0x00

    ks = [k1s,k2s,k3s,k4s]#储存当前按键状态
    Sum = chr(k1s + k2s + k3s + k4s + 0x0c)#计算校验值
    keys = b'\x57\xab\x00\x02\x08\x00\x00' + k1 + k2 + k3 + k4 + b'\x00\x00' + Sum#发送数据包
    if ks != kso :#比较按键状态
        l.on()
        uart.write(keys)#发送数据包
        l.off()
        kso = ks
    