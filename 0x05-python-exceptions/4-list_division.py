#!/usr/bin/python
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        sum = 0
        try:
            sum = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(sum)
    return new_list
