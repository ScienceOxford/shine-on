from microbit import *
from random import randint, choice
import neopixel

# Please tag us if used!
# We'd love to see what you make:
# @ScienceOxford

lights = neopixel.NeoPixel(pin0, 10)

red = (100, 0, 0)
green = (0, 100, 0)
blue = (0, 0, 100)

while True:
    # check the current temperature
    temp = temperature()
    display.scroll(temp)
    # change colour if hotter or colder than 30 degrees
    if temp >= 30:
        colour = red
    if temp < 30:
        colour = green
    for i in range(0, len(lights)):
        lights[i] = colour
    lights.show()
    sleep(1000)
