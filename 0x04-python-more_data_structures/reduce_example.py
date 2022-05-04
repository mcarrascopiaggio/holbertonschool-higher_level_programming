#!/usr/bin/python3
from functools import reduce
def weight_average(my_list=[]):
    if my_list:
        avg = map(reduce(lambda s, w: (s * w)) /w , my_list)
        return avg
    else:
        return 0
