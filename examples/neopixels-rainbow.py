from microbit import *
from random import randint, choice
import neopixel

# Please tag us if used!
# We'd love to see what you make:
# @ScienceOxford

lights = neopixel.NeoPixel(pin0, 10)

red = (50, 0, 0)
orange = (50, 25, 0)
yellow = (40, 50, 0)
chartreuse = (20, 50, 0)
green = (0, 50, 0)
teal = (0, 50, 50)
blue = (0, 0, 50)
indigo = (50, 0, 25)
violet = (50, 0, 50)
white = (50, 50, 50)

# for the below code to work, you need 10 colours in your list (one for each light)
colours = [red, orange, yellow, chartreuse, green, teal, blue, indigo, violet, white]

while True:
    for i in range(0, len(lights)):
        # set the 0th light to the 0th colour and repeat
        lights[i] = colours[i]
        lights.show()
        sleep(200)
    sleep(600)
