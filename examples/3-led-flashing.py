from microbit import *

# Please tag us if used!
# We'd love to see what you make:
# @ScienceOxford

red = pin0
green = pin1
white = pin2

while True:
    red.write_digital(1)
    green.write_digital(0)
    white.write_digital(1)
    sleep(500)
    red.write_digital(1)
    green.write_digital(1)
    white.write_digital(0)
    sleep(500)
    red.write_digital(0)
    green.write_digital(1)
    white.write_digital(1)
    sleep(500)
