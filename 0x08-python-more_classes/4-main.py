#!/usr/bin/python3
Rectangle = __import__('4-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
#str(my_rectangle)
#print(str(my_rectangle))
#print("--")
#print(my_rectangle)
#print("--")
#print(repr(my_rectangle))
#print("--")
#print(hex(id(my_rectangle)))
#print("--")

# create new instance based on representation
new_rectangle = evial(repr(my_rectangle))
#print(str(new_rectangle))
#print("--")
#print(new_rectangle)
#print("--")
#print(repr(new_rectangle))
#print("--")
#print(hex(id(new_rectangle)))
#print("--")

#print(new_rectangle is my_rectangle)
#print(type(new_rectangle) is type(my_rectangle))
