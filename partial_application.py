#partial application and currying example

from functools import partial

#fix first argument and leave the other two
def add(x,y,z):
    return x+y+z

#or
add_5 = partial(add,5)
print(add_5(6,7))


def add_partial(x):
    def add_others(y,z):
        return x+y+z

    return add_others
#---------------------------------

#we are not passing all arguments at the same time
add_5 = add_partial(5) #pass x here
print(add_5(6,7)) #pass y and z here

#fix first two arguments and leave the third argument
def add_partial2(x,y):
    def add_others(z):
        return x+y+z

    return add_others 

add_5_6 = add_partial2(5,6)
print(add_5_6(7))
#--------------------------------------

#fix first argument, next fix second argument, leave third argument:
#this is a special type of partial application called currying in 
# which one argument is applied at a time till all arguments are
#applied and final result is returned.

def curry_add(x):
    def curry_add_inner(y):
        def curry_add_inner2(z):
            return x+y+z
        return curry_add_inner2
    return curry_add_inner

add_5 = curry_add(5)
add_5_and_6 = add_5(6)
print(add_5_and_6(7))

print(curry_add(5)(6)(7))

#-------------------------
