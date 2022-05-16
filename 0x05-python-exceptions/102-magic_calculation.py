#!/usr/bin/python3
def magic_calculation(a, b):
    #LOAD_CONST 1(0)
    #STORE_FAST (result)
    result = 0
    #LOAD_GLOBAL 0(range)
    #LOAD_CONST 2(1)
    #LOAD_CONT 3(3)
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")
            else:
                result += a ** b / i
        except:
            result = a + b
            break
    return result
