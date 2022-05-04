#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    new_dic = a_dictionary.copy()
    for i in new_dic:
        new_dic[i] = a_dictionary[i] * 2
    return new_dic
