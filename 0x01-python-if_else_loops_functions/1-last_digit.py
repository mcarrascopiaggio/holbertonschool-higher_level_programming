#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    Ld = -number % 10 * -1
else:
    Ld = number % 10
st = "Last digit of"
if Ld == 0:
    print("{} {} is {} and is 0".format(st, number, Ld))
elif Ld > 5:
    print("{} {} is {} and is greater than 5".format(st, number, Ld))
else:
    print("{} {} is {} and is less than 6 and not 0".format(st, number, Ld))
