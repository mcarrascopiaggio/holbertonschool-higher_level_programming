#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lista_a = list(tuple_a)
    lista_b =list (tuple_b)
    if len(lista_a) == 0:
        lista_a.append(0)
        lista_a.append(0)
    elif len(lista_a) == 1:
        lista_a.append(0)
    if len(lista_b) == 0:
        lista_b.append(0)
        lista_b.append(0)
    elif len(lista_b) == 1:
        lista_b.append(0)
    tuple_a = tuple(lista_a)
    tuple_b = tuple(lista_b)
    add_tuple0 = tuple_a[0] + tuple_b[0]
    add_tuple1 = tuple_a[1] + tuple_b[1]
    return add_tuple0, add_tuple1

