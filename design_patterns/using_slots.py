from abc import ABCMeta, abstractmethod

# abstract
class T(metaclass=ABCMeta):
    __slots__ = ['__name'] # slots do not get inherited
    @abstractmethod
    def __init__(self, name):
        self.__name = name # we should validate

# concrete
class S(T):
    __slots__ = ['__name'] # this prevents any additional members to the instances
    def __init__(self, name):
        self.__name = name # remember: __ members are NOT inherited
    def __str__(self):
        return f'Name is {self.__name}'


# inherited 
class R(S):
    pass

if __name__ == '__main__':
    # instance of concrete
    s = S('Freda')
    # oh no, this shouldnt be allowed
    # s.__name = 'Ethel' # prevent this by using __slots__
    print(s) # untouched by outside code
    # print( s.__name ) # here is an additional arbitrary property belonging only to s

    r = R('Paula')
    r.__name = 'Sonia'
    print(r)