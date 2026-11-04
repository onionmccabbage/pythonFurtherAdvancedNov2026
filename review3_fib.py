# Fibonacci  1 1 2 3 5 8 13 21...
# always aim for performant code

# we may use cProfile to grab a profile of any running Python code
# cProfile is included with Python
# use it like this:
# python -m cProfile -o profile_output fib.py
# this will generate a profile called profile_output

import timeit
from functools import reduce

def fibA(n):
    '''Here is a low performance Fibonacci function'''
    if n in (0, 1): # if n>=1
        return 1
    else:
        '''recursively call this function again'''
        return ( fibA(n-1)+fibA(n-2) )

def fibB(n):
    '''a more performant solution'''
    sequence = (0,1)
    for _ in range(2, n+2):
        '''NB this does not mutate the existing tuple, it creates a new one'''
        sequence += (reduce( lambda a,b: a+b, sequence[-2:] ),) # careful - one-member tuple
    return sequence[-1] # access the last member of the collection

def fibC(n): # on my laptop this is fastest
    a, b = 0, 1
    for _ in range(n+1):
        a, b = b, a+b
    return a

def main():
    limit=32 # this is not too taxing
    # it is best to find an average tme when working on performance
    # fib_values_l = []
    # start1 = timeit.default_timer()
    # for n in range(2, limit+1):
    #     r = fib1(n)
    #     fib_values_l.append(r)
    # # fib1(40) took about 30 seconds on my laptop
    # end1 = timeit.default_timer()
    # print( fib_values_l ) # find the result of the first 4 members of the sequence
    # print(f'total: {end1-start1}') # about 2 seconds
    fib_values_l = []
    start2 = timeit.default_timer()
    for n in range(2, limit+1):
        r = fibB(n)
        fib_values_l.append(r)
    end2 = timeit.default_timer()
    print( fib_values_l ) # find the result of the first 4 members of the sequence
    print(f'total: {end2-start2}')
    #####
    fib_values_l = []
    start3 = timeit.default_timer()
    for n in range(2, limit+1):
        r = fibC(n)
        fib_values_l.append(r)
    end3 = timeit.default_timer()
    print( fib_values_l ) # find the result of the first 4 members of the sequence
    print(f'total: {end3-start3}')
    # print( fib2(60) ) # under 4 seconds
    start4 = timeit.default_timer()
    print( fibC(100) ) # very fast!!!
    end4 = timeit.default_timer()
    print(f'total: {end4-start4}')
    
if __name__ == '__main__':
    '''NB sometimes a different code solution is faster under differing circumstances (lower n)'''
    main()