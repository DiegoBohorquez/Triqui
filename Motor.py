from machine import Pin as pin 
from utime import sleep as pausa , sleep_ms as pausem , sleep_us as pausau 
Motor = pin ( 13 , pin.OUT ) 
A = pin ( 16 , pin . IN , pin.PULL_DOWN ) 
B = pin ( 18 , pin . IN , pin.PULL_DOWN ) 
C = pin ( 19, pin . IN , pin.PULL_DOWN ) 
Lamp = pin ( 12 , pin.OUT ) 
while True:
    H- ( A.value ( ) + B.value ( ) + C.value ( ) ) 
    if H == 3:
        Motor.value(1)
        pausem(500)
        Motor.value(0)
    elif H == 2:
        Lamp.value(1)
        Motor.value(1)
        pausem(500)
        Lamp.value(0)
        Motor.value(0)
    elif H == 1:
        Lamp.value(1)
        pausem(500)
        lamp.value(0)
