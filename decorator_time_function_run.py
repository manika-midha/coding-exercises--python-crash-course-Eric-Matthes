#using decorators, this function displays time taken to produce the output of fib()

from time import perf_counter  
from functools import wraps


def timer (func):
    @wraps(func)
    def wrapper(*args,**kwargs): #as fib is passing value, wrapper should accept that value
        start = perf_counter() #time before start of func
        result=func(*args,**kwargs)
        end = perf_counter() #time after func is run
        duration = end-start #time taken by a func to run
        arg = str(*args)
        print(f'{func.__name__}({arg}) = {result} -> {duration:.8f}s')
        #print(f'Duration:{duration:.8f}s')
        return result
    return wrapper 

@timer #decorator
def fib(n):
    '''Return the nth value from the Fiboanacci sequence'''
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

fib(4)

