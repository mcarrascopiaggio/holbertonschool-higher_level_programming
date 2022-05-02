#!/usr/bin/python3
def max_integer(my_list=[]):
    maxI = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > maxI:
            maxI = my_list[i]
    return maxI
