#!/usr/bin/python3


def weight_average(my_list=[]):
    if my_list:
        avg = 0
        divisor = list([x[0] * x[1] for x in my_list])
        dividend = list([x[1] for x in my_list])
        avg = sum(divisor) / sum(dividend)
        return avg
    else:
        return 0
