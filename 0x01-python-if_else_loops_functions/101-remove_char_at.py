#!/usr/bin/python3
def remove_char_at(str, n):
    l = len(str)
    str = str[0:n] + str[n+1:]
    print(str)
