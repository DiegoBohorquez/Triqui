from machine import Pin as pin
from utime import sleep as pausa, sleep_ms as pausem, sleep_us as pausau
led1 = pin(13,pin.OUT)
led2 = pin(12,pin.OUT)
led3 = pin(14,pin.OUT)
led4 = pin(27,pin.OUT)
led5 = pin(26,pin.OUT)
led6 = pin(25,pin.OUT)
led7 = pin(15,pin.OUT)
led8 = pin(2,pin.OUT)
led9 = pin(4,pin.OUT)
led10 = pin(5,pin.OUT)
botoncito1 = pin(16,pin.IN, pin.PULL_DOWN)
botoncito2 = pin(18,pin.IN, pin.PULL_DOWN)
botoncito3 = pin(19,pin.IN, pin.PULL_DOWN)
botoncito4 = pin(21,pin.IN, pin.PULL_DOWN)
def print_led(a, b, c, d, e, f, g, h, i, j):
    led1.value(a)
    led2.value(b)
    led3.value(c)
    led4.value(d)
    led5.value(e)
    led6.value(f)
    led7.value(g)
    led8.value(h)
    led9.value(i)
    led10.value(j)
    pausem(200)
    pausa = 2
puerto=[13, 12, 14, 27, 26, 25, 15, 2, 4, 5]
ledt = [led1, led2, led3, led4, led5, led6, led7, led8, led9, led10]
ledta = [led2, led1, led5, led3, led9, led8, led10, led7, led9, led4]
ledte = [led10, led8, led4, led3, led9, led5, led6, led1, led2, led7]
ledti = [led5, led1, led9, led10, led7, led6, led2, led4, led3, led8]
ledto = [led8, led2, led7, led4, led5, led3, led6, led9, led1, led10]
ledtu = [led4, led2, led5, led1, led10, led3, led8, led9, led7, led6]
n=300    
while True:

    if (botoncito1.value()):
        for i in ledt:
            for j in range (2):
                 i.value(not i.value())
                 pausem(n)
            e = n + 100         
    if (botoncito2.value()):
        for i in reversed (ledt):
             for j in range (2):
                 i.value(not i.value())
                 pausem(n)
             e = n - 100     
    if (botoncito3.value()):
            print_led(0,0,0,0,1,1,0,0,0,0)
            print_led(0,0,0,1,0,0,1,0,0,0)
            print_led(0,0,1,0,0,0,0,1,0,0)
            print_led(0,1,0,0,0,0,0,0,1,0)
            print_led(1,0,0,0,0,0,0,0,0,1)
            print_led(0,1,0,0,0,0,0,0,1,0)
            print_led(0,0,1,0,0,0,0,1,0,0)
            print_led(0,0,0,1,0,0,1,0,0,0)
            print_led(0,0,0,0,1,1,0,0,0,0)
            print_led(0,0,0,0,0,0,0,0,0,0)
    if (botoncito4.value()):
            led1.value(1)
            (pausau)
            led1.value(0)
            led2.value(1)
            (pausem)
            led2.value(0)
            led3.value(1)
            (pausau)
            led3.value(0)
            led4.value(1)
            (pausau)
            led4.value(0)
            led5.value(1)
            (pausem)
            led5.value(0)
            led6.value(1)
            (pausau)
            led6.value(0)
            led7.value(1)
            (pausau)
            led7.value(0)
            led8.value(1)
            (pausau)
            led8.value(0)
            led9.value(1)
            (pausem)
            led9.value(0)
            led10.value(1)
            (pausau)
            led10.value(0)
            (pausau)
    if (botoncito1.value() and botoncito2.value()):
            print_led(1,0,0,0,0,1,0,0,0,0)
            print_led(0,1,0,0,0,0,1,0,0,0)
            print_led(0,0,1,0,0,0,0,1,0,0)
            print_led(0,0,0,1,0,0,0,0,1,0)
            print_led(1,0,0,0,1,0,0,0,0,1)
            print_led(0,1,0,0,0,1,0,0,0,0)
            print_led(0,0,1,0,0,0,1,0,0,0)
            print_led(0,0,0,1,0,0,0,1,0,0)
            print_led(0,0,0,0,1,0,0,0,1,0)
            print_led(0,0,0,0,0,0,0,0,0,0)

    if (botoncito3.value() and botoncito4.value()):
            print_led(1,0,0,0,0,1,0,0,0,0)
            print_led(0,1,0,0,0,0,1,0,0,0)
            print_led(0,0,1,0,0,0,0,1,0,0)
            print_led(0,0,0,1,0,0,0,0,1,0)
            print_led(1,0,0,0,1,0,0,0,0,1)
            print_led(0,1,0,0,0,1,0,0,0,0)
            print_led(0,0,1,0,0,0,1,0,0,0)
            print_led(0,0,0,1,0,0,0,1,0,0)
            print_led(0,0,0,0,1,0,0,0,1,0)
            print_led(0,0,0,0,0,0,0,0,0,0)
    
     
    if (botoncito2.value() and botoncito3.value()):  
            for i in ledta:
                for j in range (8):
                    i.value(not i.value())
                    pausem(e)
    if (botoncito1.value() and botoncito4.value()):   
            for i in reversed (ledta):
                for j in range (10):
                    i.value(not i.value())
                    pausem(e)

    if (botoncito1.value() and botoncito3.value()):
            for i in ledte:
                for j in range (16):
                    i.value(not i.value())
                    pausem(e)
        
    if (botoncito2.value() and botoncito4.value()):
            for i in reversed (ledte):
                for j in range (7):
                    i.value(not i.value())
                    pausem(e)

    if (botoncito1.value() and botoncito2.value() and botoncito4.value()):
            for i in ledti:
                for j in range (16):
                    i.value(not i.value())
                    pausem(e)

    if (botoncito1.value() and botoncito2.value() and botoncito3.value()):
            for i in reversed (ledti):
                for j in range (6):
                    i.value(not i.value())
                    pausem(e)

    if (botoncito2.value() and botoncito3.value() and botoncito4.value()):
            for i in ledto:
                for j in range (3):
                    i.value(not i.value())
                    pausem(e)

    if (botoncito1.value() and botoncito3.value() and botoncito4.value()):
            for i in reversed (ledti):
                for j in range (4):
                    i.value(not i.value())
                    pausem(e)

    if (botoncito1.value() and botoncito2.value() and botoncito3.value() and botoncito4.value()):
            for i in ledtu:
                for j in range (5):
                    i.value(not i.value())
                    pausem(e)