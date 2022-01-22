#!/usr/bin/python3
def add_integer(a, b=98):

    """ 
    function that adds 2 integers 
    >>> add_integer(2,3)
    5
    >>> add_integer(2.0,4)
    6
    >>> add_integer('hola', 2)
    Traceback (most recent call last):
    TypeError: a must be an integer
    
    >>> add_integer(2,'hola')
    Traceback (most recent call last):
    TypeError: b must be an integer
    """
    if type(a) is not int:
        if type(a) is not float:
            raise TypeError("a must be an integer")
        else: 
            a = int(a)

    if type(b) is not int:
        if type(b) is  not float:
            raise TypeError("b must be an integer")
        else:
            b = int(b)
    else:
        return (a + b)
