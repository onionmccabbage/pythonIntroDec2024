# We need to encapsulate temperature and data-through-put (Baud) for a device

class Device: # by convention we use InitialCap
    '''temp in celcius and baud will be persisted in this class'''
    def __init__(self, t, b): # the initializer for this class (like a constructor)
        self.t = self.temperature(t)
        self.b = b
    # an advantage of a class is we can validate the data members
    # All methods take 'self' as an argument
    def temperature(self, new_t): # this function is a method of this class
        '''validate the temperature is an int or a float. Raise exception if not'''
        if type(new_t) in (int, float):
            return new_t
        else:
            raise Exception('Temperature must be a number')
    def baud(self, new_b):
        '''validate the baud as a positive int or float'''
        # NB check the type before checking it's bigger than zero!!
        if type(new_b) in (int, float) and new_b>0 :
            return new_b
        else:
            raise Exception('Baud must be a positive number')
    def __str__(self):
        '''__str__ is used by any print statement'''
        return f'This Device is at {self.t}Celcius Baud rate is {self.b}'


if __name__ == '__main__':
    # we can make instances of our class
    d1 = Device(12.5, 886) # the __init__ function is called every time we make an instance
    print(d1, type(d1), d1.t, d1.b) # this will vall the __str__ method
    # d2 = Device('hot', 'fast') # expect an exception