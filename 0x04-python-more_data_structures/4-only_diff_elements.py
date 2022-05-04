#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    l1 = list(set_1)
    l2 = list(set_2)
    l12 = l1 + l2
    uniquel12 = set(l12)
    return uniquel12
