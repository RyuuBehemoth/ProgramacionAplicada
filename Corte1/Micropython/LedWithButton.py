from machine import Pin
from time import sleep

led = Pin(14, Pin.OUT)
push_button = Pin(12, Pin.IN)

#Mantiene el boton para encender el led y se apaga si lo suelta
while True:
  logic_state = push_button.value()
  if logic_state == True:
      led.value(1)
  else:
      led.value(0)

#Presiona el boton una vez para encender y otra para apagar
while True:
    logic_state = push_button.value()
    if logic_state == True:
        if led.value() == 0:
            led.value(1)
        else:
            led.value(0)