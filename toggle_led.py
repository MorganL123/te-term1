from gpiozero import LED
from time import sleep

led = LED(17)


while True:
    in = input("Type on or off")
    if in == "on"
    led.on()
    elif in = "off":
    led.off()