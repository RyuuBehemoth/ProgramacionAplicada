import machine
import utime

led_pins = [15,2,4,5,18,19,21,22]
leds = [machine.Pin(pin,machine.Pin.OUT) for pin in led_pins]

while True:
    for led in leds:
        led.value(1)
        utime.sleep(0.5)
        led.value(0)
