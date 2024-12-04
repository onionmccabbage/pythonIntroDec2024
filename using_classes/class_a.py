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
            self.t = new_t
        else:
            raise Exception('Temperature must be a number')

if __name__ == '__main__':
    # we can make instances of our class
    d1 = Device(12.5, 886) # the __init__ function is called every time we make an instance
    print(d1, type(d1), d1.t, d1.b)