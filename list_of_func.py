#displays the use of functions in a list
import math

def double(x):
    return x *2

def minus_one(x):
    return x-1

def square(x):
    return x ** 2

func_list = [
    double,
    minus_one,
    square,
    math.sqrt #calculates square root
    ]

my_num = 3
for func in func_list:
    my_num=func(my_num)

print (my_num)
