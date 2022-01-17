#!/usr/bin/python3
# function that prints x elements of a list.
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        for i in range(x):
            print("{:d}".format(my_list[i]), end="")
            i = i + 1
    except Exception as ex:
        pass
    print()
    return i
