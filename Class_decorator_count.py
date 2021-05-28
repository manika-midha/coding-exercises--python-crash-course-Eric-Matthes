#create a class that counts the number of times a call 
# is made to Fibonacci function
from functools import update_wrapper

#class is used like a decorator func
class Count():
    def __init__(self,func):
        update_wrapper(self,func) #purpose is to have correct func name and doc string
        self.func = func
        self.cnt = 0

    #make a class callable : this func is run each time an instance of the class is called.
    #this is like the wrapper func
    def __call__(self,*args,**kwargs):
        self.cnt+=1
        print(f'Current count:{self.cnt}') 
        result=self.func(*args,**kwargs)
        return result

@Count
def fib(n):
    ''' return the Fibonacci sequence '''
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

fib(4)



