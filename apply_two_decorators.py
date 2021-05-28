#apply two decorators to a function.
from functools import wraps

def bold (func):
    @wraps(func)
    def wrapper():
        result ='<b>' + func() + '</b>'
        return result
    return wrapper 

def italic (func):
    @wraps(func)
    def wrapper():
        result ='<i>' + func() + '</i>'
        return result
    return wrapper 


@bold
@italic
def printfib():
    '''return Fibonacci'''
    return 'Fibonacci'

print(printfib())