x=10
y=10

def compare():
    global x, y
    if id(x) == id(y):
        print(f' x and y refer to the same object in memory: {id(x)} {id(y)}')
    else:
        print(f' x and y refer to different objects in memory: {id(x)} {id(y)}')

if __name__ == '__main__':
    compare()
    x +=1
    compare()
    y +=1
    compare()
    # therefore it is sometimes performance to prepare memory that contains values wie will need!
    # e.g. min, max, facets to use in comparators...
    # NB some things always exist in memory, such as zero
    # sometimes it is (very slightly) faster to loop down to zero
    l1=(9,8,7,6,5,4,3,2,1,0)
    l2=(0,1,2,3,4,5,6,7,8,9)
    for _ in l1:
        print (_)

    