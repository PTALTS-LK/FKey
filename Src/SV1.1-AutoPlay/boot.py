'''
Fkey
Copyright (C) 2022 PCX-LK

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''
#项目主页github.com/PCX-LK/FKey
#Powered by PCX-LK
#V1.1-Autoplay

from machine import UART,Pin
import time

uart = UART(2, baudrate=9600, tx=17, rx=16)#初始化uart通信
sw1 = Pin(32, Pin.IN, Pin.PULL_UP)#初始化引脚
sw2 = Pin(33, Pin.IN, Pin.PULL_UP)
sw3 = Pin(25, Pin.IN, Pin.PULL_UP)
sw4 = Pin(26, Pin.IN, Pin.PULL_UP)
bk = Pin(27, Pin.IN, Pin.PULL_UP)
AP = Pin(18, Pin.IN, Pin.PULL_UP)
l = Pin(2, Pin.OUT)#初始化LED发包指示灯

k1s = k2s = k3s = k4s = 0x00#预定义变量
k1ms = k2ms = k3ms = k4ms = 0
kso = [k1s,k2s,k3s,k4s]

startP = 0
ssP = 0
file = open('Play.txt')
lines = file.readlines()
te = 0
wait = 0

#4个键的默认键码（默认dfjk），可自行更改，参见Docs/CH9329串口通信协议->附录1 “CH9329键码表”（HID Code）
k1def = 0x07
k2def = 0x09
k3def = 0x0d
k4def = 0x0e

while 1 :
    if bk.value() == 0 :
        break
    if AP.value() == 1 :
        l.off()
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
        keys = b'\x57\xab\x00\x02\x08\x00\x00' + k1 + k2 + k3 + k4 + b'\x00\x00' + Sum#合并数据包
        if ks != kso :#比较按键状态
            l.on()
            uart.write(keys)#发送数据包
            l.off()
            kso = ks


    else :
        l.on()
        sP = 0
        if sw2.value() == 0 :
            startP = 1
        while startP == 1 :
            if sw3.value() == 0 :
                startP = 0
            if time.ticks_diff(time.ticks_ms(), te) >= wait :
                wait = int(lines[sP][0:len(lines[sP])-1])#读取，“-1”是减去\n的占位
                k1s = int(lines[sP+1][0:len(lines[sP+1])-1])
                k2s = int(lines[sP+2][0:len(lines[sP+2])-1])
                k3s = int(lines[sP+3][0:len(lines[sP+3])-1])
                if sP + 4 == len(lines) - 1 :#判断是否是最后一行
                    k4s = int(lines[sP+4][0:len(lines[sP+4])])
                    startP = 0
                else :
                    k4s = int(lines[sP+4][0:len(lines[sP+4])-1])
                k1 = chr(k1s)
                k2 = chr(k2s)
                k3 = chr(k3s)
                k4 = chr(k4s)
                te = time.ticks_ms()
                Sum = chr(k1s + k2s + k3s + k4s + 0x0c)#计算校验值
                keys = b'\x57\xab\x00\x02\x08\x00\x00' + k1 + k2 + k3 + k4 + b'\x00\x00' + Sum#合并数据包
                l.on()
                uart.write(keys)
                l.off()
                sP += 5
