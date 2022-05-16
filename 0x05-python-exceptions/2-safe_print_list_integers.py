#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    nb_print = 0
    try:
        for i in range(x):
            if type(my_list[i] == int):
                print("{:d}".format(my_list[i]), end="")
                nb_print = nb_print + 1
        print()
    except Exception:
        pass
    return(nb_print)