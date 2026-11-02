# Polymorphism lets things behave in several ways

def builtInPol():
    '''Many Python features are already polymorphic'''
    print( len([1,2,3]) )   # len of a list
    print( len((1,2,3)) )   # len of a tuple
    print( len('hello') )   # len of a string
    # many Python featrues will change their behaviour in context
    print( max(1,2,3) )    # maximum of a single data type collection
    print( max('a', 'b', 'c') )

class Multiplier:
    '''for any and all numeric entries, return the product (i.e. multiply them all together)
    NB other languages have overloading, but not in Python'''
    def multiply(self, a=1, b=1, *args): # *args is any additional positional arguments
        result = a*b                     # **kwargs is also available: dict of keyword arguments
        for _ in args:
            result *= _
        return result

# Polymorphism can be implemented with cutom object types
class Pen:
    '''this type will be used for writing'''
    def use(self):
        '''Any class to be used as a type will implement the 'use' method'''
        return 'writing'

class Eraser:
    '''this type will be used for erasing'''
    def use(self):
        return 'erasing'

# we may choose to specify a return type. Python does not implement the type check at runtime
# This is for dev-time tools which may catch type problems
# Pycharm has tools to warn of type problems
def performTask(tool:object)->str:
    '''use a (typed) tool to perform a task'''
    # this may also involve conditional logic
    print( tool.use() )

if __name__ == '__main__':
    builtInPol()
    mult = Multiplier()
    print( mult.multiply() ) # 1
    print( mult.multiply(1,2,3) ) # *args will contain (3,) a tuple
    print( mult.multiply(1,2,3,4,5,6,7,8,9) ) # *args will contain a tuple
    #########
    performTask(Pen())
    performTask(Eraser())