from time import perf_counter
from functools import wraps,lru_cache 

#lru_cache() is one such function in functools module which helps in reducing the 
# execution time of the function by using memoization technique. it takes function
#as an argument.Syntax = @lru_cache (maxsize=128,typed=False).maxsize:This parameter sets the
# size of the cache, the cache can store upto maxsize most recent function calls, 
# if maxsize is set to None, the LRU feature will be disabled and the cache can grow 
# without any limitations


def timer(func):
    total = 0 # scope: timer()
    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal total
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        duration = end - start
        total += duration #scope : wrapper()
        arg = str(*args)
        print(f'{func.__name__}({arg}) = {result} -> {duration:.8f}')
        #print(f'Total duration: {total:.8f}')
        return result
    return wrapper

@lru_cache(None)
@timer
def fib(n):
    '''Return the nth value from the Fiboanacci sequence'''
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

fib(18)

#Dunder or magic methods in Python are the methods having two prefix
# and suffix underscores in the method name. Dunder here means “Double Under (Underscores)”. 
# These are commonly used for operator overloading. Few examples for magic
# methods are: __init__, __add__, __len__, __repr__ etc.
#The __init__ method for initialization is invoked without any call, when an 
# instance of a class is created