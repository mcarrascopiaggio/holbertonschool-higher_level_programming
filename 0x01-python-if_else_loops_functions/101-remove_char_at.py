#!/usr/bin/python3
def remove_char_at(str, n):
    large = len(str)
    if n > 0 and n <= large:
        str = str[0:n] + str[n+1:]
        return (str)
    else:
        return(str)
