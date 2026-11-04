# Range, Generators and Comprehension
# These features are impressively performant
# they are designed to help memory efficiency

# the range object exists in memory but all the values are provided on demand (not in memory)
r = range(-10**4, 10**4, 100) # start=0, stop-before, step=1
for _ in r:
    print( _, end=', ' ) # by default print terminates with a new line character

def doStuff(n):
    return ((n-1)/(n+1))**0.5

# generators apply some functinoality to every member in a collection
g = (doStuff(i) for i in r) # or any iterator
print(g, type(g))
# the results of all the generator values do not exist in memory
# we may access values fro ma generator
print( g.__next__() )
print( g.__next__() )
print( g.__next__() )
print( g.__next__() )
# for _ in g:
#     print( _, end=', ' )

# comprehension: deal with every member of a collection comprehensively
c = [doStuff(i) for i in r] # this is a list comprehension
print(c) # we have a list
