from machine import Pin as pin,ADC,I2C
from utime import sleep_ms
from ssd1306 import SSD1306_I2C
import framebuf

color = 1

sensorx = ADC(pin(32))   # pines usados el 35,34,33,36, 39 , 32, 
sensory = ADC(pin(33))   # pines usados el 35,34,33,36, 39 , 32, 

sensorx.atten(ADC.ATTN_11DB)   # para calibrar de 0 a 3.6v
sensorx.width(ADC.WIDTH_12BIT) # establecer resolución
sensory.atten(ADC.ATTN_11DB)   # para calibrar de 0 a 3.6v
sensory.width(ADC.WIDTH_12BIT) # establecer resolución


ancho = 128
alto = 64
i2c = I2C(0, scl=pin(22), sda=pin(23))
oled = SSD1306_I2C(ancho, alto, i2c)
# print(i2c.scan())

boton = pin(13,pin.IN, pin.PULL_UP)
led = pin(2,pin.OUT)

movimientoX = 16
movimientoY = 15

modulo = 2
a = 0
b = 0

while True:


  quedaEscrito = a

  while b==0:

    led.value(boton.value())

    x=sensorx.read()
    y=sensory.read()
    #oled.fill(1)
    oled.text("TRIQUI", 41, 00,color)

    #verticales
    oled.line(42,10,42,64,1)
    oled.line(85,10,85,64,1)
    
    #Horizontales
    oled.line(0,47,128,47,1)
    oled.line(0,27,128,27,1)

    #x
    #oled.line(0,10,38,25,1)
    #led.line(0,25,38,10,1)

    equis = oled.text("X", movimientoX, movimientoY,color)

  #Izquierda
    if x>3600:
      movimientoX = movimientoX-44 
      if movimientoX<16:
        movimientoX=16
          
      oled.text("X", movimientoX, movimientoY,color)
  #Derecha
    elif x<150:
      movimientoX = movimientoX+44 
      if movimientoX>104:
        movimientoX=104

      oled.text("X", movimientoX, movimientoY,color)

  #Arriba
    if y>3600:
      movimientoY = movimientoY-20 
      if movimientoY<15:
        movimientoY=15
          
      oled.text("X", movimientoX, movimientoY,color)
      
  #Abajo    
    elif y<150:
      movimientoY = movimientoY+20
      if movimientoY>56:
        movimientoY=56

      oled.text("X", movimientoX, movimientoY,color)
    
    
    if boton.value()==0:
      #modulo = modulo+1
      oled.text("X", movimientoX, movimientoY,color)
      a = oled.text("X", movimientoX, movimientoY,color)
      b=1
      
    oled.show()
    sleep_ms(200)

    #if modulo%2==0:
    
    oled.fill(0)



  #while 2
  while b==1:

    led.value(boton.value())

    x=sensorx.read()
    y=sensory.read()
    #oled.fill(1)
    oled.text("TRIQUI", 41, 00,color)

    #verticales
    oled.line(42,10,42,64,1)
    oled.line(85,10,85,64,1)
    
    #Horizontales
    oled.line(0,47,128,47,1)
    oled.line(0,27,128,27,1)

    #x
    #oled.line(0,10,38,25,1)
    #led.line(0,25,38,10,1)

    equis = oled.text("O", movimientoX, movimientoY,color)

  #Izquierda
    if x>3600:
      movimientoX = movimientoX-44 
      if movimientoX<16:
        movimientoX=16
          
      oled.text("O", movimientoX, movimientoY,color)
  #Derecha
    elif x<150:
      movimientoX = movimientoX+44 
      if movimientoX>104:
        movimientoX=104

      oled.text("O", movimientoX, movimientoY,color)

  #Arriba
    if y>3600:
      movimientoY = movimientoY-20 
      if movimientoY<15:
        movimientoY=15
          
      oled.text("O", movimientoX, movimientoY,color)
      
  #Abajo    
    elif y<150:
      movimientoY = movimientoY+20
      if movimientoY>56:
        movimientoY=56

      oled.text("O", movimientoX, movimientoY,color)
    
    
    if boton.value()==0:
      modulo = modulo+1
      oled.text("O", movimientoX, movimientoY,color)
      a = oled.text("O", movimientoX, movimientoY,color)
      b = 0
      
    oled.show()
    sleep_ms(200)
