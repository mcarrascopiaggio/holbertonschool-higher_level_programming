#!/usr/bin/python3
def element_at(my_list, idx):
    lg = len(my_list)
    if idx < 0 or idx >= lg:
        return None
    else:
        return my_list[idx]
