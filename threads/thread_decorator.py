from threading import Thread, Lock, Semaphore, current_thread

lk = Lock()

# higher-order functions: where one function contains another function
def lock_a_method(meth):
    '''this function will act as a decorator for any other method
    it will check if the method is already thread locked
    If not it will acquire a lock then release it after
    '''
    global lk
    def locked_method(self, *args, **kwargs):
        '''this will be a locked version of the method'''
        # check if there is an attribute indicated locked
        # we may provide a default as follows
        can_use_lock = getattr(meth, '__use_lock', False) # return True or False
        if can_use_lock:
            pass
        else:
            with lk:
                print('locking (and releasing)')
                return meth(self, *args, **kwargs) # NB ** will only pass kwargs if there are any
            # when the 'with' ends, the lock is released automatically
    locked_method.__use_lock = True # attach an arbitrary value to the method
    return locked_method


# here is a class with methods we may wish to lock
class MySet(set): # we now have our own 'set' type
    def __init__(self, iterable):
        super().__init__(iterable)
    @lock_a_method
    def intAdd(self, new_int):
        '''check the value is an int before adding to the set'''
        if type(new_int)==int:
            super().add(new_int)
        else:
            # raise TypeError('not an integer')
            print('not an integer')

if __name__ == '__main__':
    s = {4,2,8,5,9,4} # colection of unique data members
    myset = MySet(s)
    myset.add(0)
    myset.remove(8)
    myset.intAdd(55)
    myset.intAdd('55') # not added
    print(myset, type(myset))
    # what is a set in Python
    # t = {'zeb', 'betie', 'carrie', 'aleph'} # colection of unique data members
    # s.add(0)
    # s.remove(2)
    # print(s, type(s))
    # print(t, type(t))
