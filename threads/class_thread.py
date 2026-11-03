from threading import Thread
import random
import time

class MyClass():
    '''We will call instances of this class on separate threads'''

    def __call__(self, n):
        '''in order to use a class on a thread, we MUST implement __call__ '''
        for i in range(0,6):
            print(f'{n} is working...')
            time.sleep(random.random()*0.1 )

def main():
    '''invoke class instances on threads'''
    c1 = MyClass() # we have an instance of the class
    t1 = Thread(target=c1, kwargs={'n':1}) # keyword args are always a dict
    t2 = Thread(target=c1, kwargs={'n':2})
    t3 = Thread(target=c1, kwargs={'n':3})
    t1.start()
    t2.start()
    t3.start()
    # if we choose we may pause the main thread...
    t1.join()
    t2.join()
    t3.join()


if __name__ == '__main__':
    main()