# Imports go at the top
from microbit import *
from random import randint, choice
import neopixel

lights = neopixel.NeoPixel(pin0, 10)

red = (100, 0, 0)
green = (0, 100, 0)
blue = (0, 0, 100)



# Code in a 'while True:' loop repeats forever
while True:
    display.show(Image.HEART)
    sleep(1000)
    display.scroll('Hello')
