from machine import UART,Pin
import time
#Ver1.0
uart = UART(2, baudrate=9600, tx=17, rx=16)
sw1 = Pin(27, Pin.IN, Pin.PULL_UP)
sw2 = Pin(26, Pin.IN, Pin.PULL_UP)
sw3 = Pin(33, Pin.IN, Pin.PULL_UP)
sw4 = Pin(32, Pin.IN, Pin.PULL_UP)
bk = Pin(25, Pin.IN, Pin.PULL_UP)
l = Pin(2, Pin.OUT)

k1s = k2s = k3s = k4s = 0x00
a = 0
kso = [k1s,k2s,k3s,k4s]
Sum = 0x0c

while a == 0 :
    k1 = k2 = k3 = k4 = b'\x00'
    k1s = k2s = k3s = k4s = 0x00
    
    if bk.value() == 0 :
        break
    if sw1.value() == 0 :
        k1 = b'\x07'
        k1s = 0x07
    if sw2.value() == 0 :
        k2 = b'\x09'
        k2s = 0x09
    if sw3.value() == 0 :
        k3 = b'\x0d'
        k3s = 0x0d
    if sw4.value() == 0 :
        k4 = b'\x0e'
        k4s = 0x0e
    ks = [k1s,k2s,k3s,k4s]
    SumR = chr(k1s + k2s + k3s + k4s + Sum)
    keys = b'\x57\xab\x00\x02\x08\x00\x00' + k1 + k2 + k3 + k4 + b'\x00\x00' + SumR
    if ks != kso :
        l.on()
        uart.write(keys)
        l.off()
        kso = ks
    
