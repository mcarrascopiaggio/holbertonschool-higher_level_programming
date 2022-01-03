#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    lg = len(my_list)
    for i in range(lg):
        print("{:d}".format(my_list[-i-1]))
