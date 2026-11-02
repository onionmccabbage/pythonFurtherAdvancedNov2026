# All decorators use the @ sign

# here is a function to be used as a custom decorator
def showArgs(func:function):
    '''reveal all the args and kwargs passed in to func'''
    def newFunc(*args, **kwargs): # args is always a tuple kwargs is always a dict
        '''expose the args and kwargs'''
        print(f'''Positional arguments are: {args}
Keyword arguments are: {kwargs}''')
        # we need to execute the original function
        return func(*args, **kwargs)
    return newFunc # the decorator returns our new function

# here is a simple function
@showArgs # this is how we use a decorator
def squares(m,n):
    '''return a list of the squares of m to n'''
    s = []
    for _ in range(m, n):
        s.append(_*_)
    return s


if __name__ == '__main__':
    print(squares(1,11))