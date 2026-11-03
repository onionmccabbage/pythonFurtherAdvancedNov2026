# we often need to work with large quantities of values
# the range object is very efficient for this

# range will generate the values as needed, so memory does not get wasted 
r = range(10_000, -10_000, -5) # start, stop-before, step

for _ in r:
    print(_)