# here we explore ways to find the fibonacci sequence
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

import timeit
import time
from functools import reduce

def fibA(n):
    '''a known-low-performance technique'''
    if n in (0, 1):
        return 1 # fib(0) and fib(1) always result in 1
    else:
        # we recursively call this SAME function
        return ( fibA(n-1) + fibA(n-2) )

def fibB(n):
    '''a more performant approach'''
    seq = (0,1) # tuple - immutable
    for _ in range(2, n+2):
        # reduce will repeatedly apply a function resolving to one result
        # lambda lets us write an in-place function
        seq += (reduce( lambda a,b:a+b, seq[-2:] ),) # a one-member tuple must have a trailing comma
    return seq[-1] # return the last member of our sequence

if __name__ == '__main__':
    startA = time.perf_counter()
    print( fibA(32) )
    endA = time.perf_counter()

    startB = time.perf_counter()
    print( fibB(32) )
    endB = time.perf_counter()

    print(f'A: {endA-startA} B: {endB-startB}')