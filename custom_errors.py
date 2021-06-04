#this file shows how to make custom exceptions/errors

class ElectricalError(Exception):
    """custom Electrical error """
    def __init__(self, device,problem) :
        self.device = device
        self.problem = problem

    def __str__(self):
         """this function overrides the __str__ function of the Exception class """
        return f'the {self.device} is {self.problem}'

class PlumbingError(Exception):
    """custom Plumbing error """
    def __init__(self, device,problem) :
        self.device = device
        self.problem = problem

    def __str__(self):
        """this function overrides the __str__ function of the Exception class """
        return f'the {self.device} is {self.problem}'

def cause_error(errortype):
    """this function raises exception based on the error type passed """

    if errortype=='electrical':
        raise ElectricalError ('circuit breaker','over-loaded')
    elif errortype == 'plumbing':
         raise PlumbingError ('dishwasher','spraying water')
    else :
        raise Exception ('some other problem')

try :
    cause_error()

except ElectricalError as e :
    print(e) #this is the string message defined in the --str-- function in the ElectricalError class
    print('fixing it myself')
    
except PlumbingError as e :
    print(e) #this is the string message defined in the --str-- function in the PlumbingError class
    print('need to call plumber')

except : #handle all exceptions other than electrical and plumbing
    print('call landlord')