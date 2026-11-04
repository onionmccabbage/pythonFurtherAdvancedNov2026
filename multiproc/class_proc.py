from multiprocessing import Process
import random
import time
import os


class MyClass():
    '''We will call instances of this class on separate threads'''

    def __call__(self, n):
        '''in order to use a class on a process, we MUST implement __call__ '''
        for i in range(0,6):
            print(f'{n} is working...')
            time.sleep(random.random()*0.1 )

def main():
    '''invoke class instances on processes'''
    c1 = MyClass() # we have an instance of the class
    n_proc = os.cpu_count()-1
    procs = []
    for _ in range(n_proc):
        p = Process(target=c1, kwargs={'n':_})
        p.start()
        procs.append(p)
    # if we choose we may pause the main process...
    for _ in procs:
        _.join()


if __name__ == '__main__':
    main()