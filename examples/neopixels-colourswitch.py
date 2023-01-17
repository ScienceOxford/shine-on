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

colours = [red, green, blue]

# repeat forever
while True:
    
    # turn all the lights blue
    for i in range(0, len(lights)):
        lights[i] = blue
        lights.show()

    # stay blue for 2 seconds
    sleep(2000)

    # turn all the lights red
    for i in range(0, len(lights)):
        lights[i] = red
        lights.show()

    # stay red for 2 seconds
    sleep(2000)
