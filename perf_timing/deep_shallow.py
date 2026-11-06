import copy

a = [ [1,2,3],[4,5,6] ]
b = a # both refer to the same thing

b[0][0] = 99
print(a)

# shallow copy
c = copy.copy(a)
c[0][0]=999
print(a)
d = copy.deepcopy(a) # a complete new in-memory copy
d[1][0] = 99
print(a, b, c, d)