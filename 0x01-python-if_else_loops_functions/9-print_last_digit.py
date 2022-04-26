#!/usr/bin/env python3
def print_last_digit(number):
    if number < 0:
        number = number * -1
    Ld = number % 10
    print("{}".format(Ld), end="")
    return(Ld)
