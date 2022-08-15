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

from machine import UART,Pin
import time
#
uart = UART(2, baudrate=9600, tx=17, rx=16)
sw1 = Pin(27, Pin.IN, Pin.PULL_UP)
sw2 = Pin(26, Pin.IN, Pin.PULL_UP)
sw3 = Pin(33, Pin.IN, Pin.PULL_UP)
sw4 = Pin(32, Pin.IN, Pin.PULL_UP)
bk = Pin(25, Pin.IN, Pin.PULL_UP)
l = Pin(2, Pin.OUT)

a = 0
k1s = k2s = k3s = k4s = 0x00
k1ms = k2ms = k3ms = k4ms = 0
Sum = 0x0c
kso = [k1s,k2s,k3s,k4s]

#k1s = 
#k2s = 
#k3s = 
#k4s = 

while a == 0 :
    if bk.value() == 0 :
        break
    if sw1.value() == 0 :
        k1 = b'\x07'
        k1s = 0x07
        k1ms = time.ticks_ms()
    elif time.ticks_diff(time.ticks_ms(), k1ms) >= 5 :
        k1 = b'\x00'
        k1s = 0x00

    if sw2.value() == 0 :
        k2 = b'\x09'
        k2s = 0x09
        k2ms = time.ticks_ms()
    elif time.ticks_diff(time.ticks_ms(), k2ms) >= 5 :
        k2 = b'\x00'
        k2s = 0x00

    if sw3.value() == 0 :
        k3 = b'\x0d'
        k3s = 0x0d
        k3ms = time.ticks_ms() 
    elif time.ticks_diff(time.ticks_ms(), k3ms) >= 5 :
        k3 = b'\x00'
        k3s = 0x00
    
    if sw4.value() == 0 :
        k4 = b'\x0e'
        k4s = 0x0e
        k4ms = time.ticks_ms()
    elif time.ticks_diff(time.ticks_ms(), k4ms) >= 5 :
        k4 = b'\x00'
        k4s = 0x0e

    ks = [k1s,k2s,k3s,k4s]
    SumR = chr(k1s + k2s + k3s + k4s + Sum)
    keys = b'\x57\xab\x00\x02\x08\x00\x00' + k1 + k2 + k3 + k4 + b'\x00\x00' + SumR
    if ks != kso :
        l.on()
        uart.write(keys)
        l.off()
        kso = ks
    
