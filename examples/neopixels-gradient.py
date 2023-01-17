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

amount_green = 10
amount_red = 190
for pixel in range(0, len(lights)):
    lights[pixel] = (amount_red, amount_green, 0)
    amount_green += 20
    amount_red -= 20
lights.show()
