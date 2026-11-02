# Polymorphism lets things behave in several ways

def builtInPol():
    '''Many Python features are already polymorphic'''
    print( len([1,2,3]) )   # len of a list
    print( len((1,2,3)) )   # len of a tuple
    print( len('hello') )   # len of a string
    # many Python featrues will change their behaviour in context
    print( max(1,2,3) )    # maximum of a single data type collection
    print( max('a', 'b', 'c') )



if __name__ == '__main__':
    builtInPol()