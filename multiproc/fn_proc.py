from multiprocessing import Process

# we will use these to simulate long-running operations
import random
import time

def myFn(n):
    for i in range(0,6):
        print(f'{n} is working...')
        time.sleep(random.random()*0.1 )

# use multiprocessing when the resources are external to Python
# since processes do not hsare Python resources
# how many threads? .... how many processes....?

def main():
    '''create a number of threads each using our function'''
    t1 = Process(target=myFn,args=(1,)) # args is always a tuple (here a one-member tuple)
    t2 = Process(target=myFn,args=(2,)) # args is always a tuple (here a one-member tuple)
    t3 = Process(target=myFn,args=(3,)) # args is always a tuple (here a one-member tuple)
    # at any moment we may choose to sequentialy start the process
    t1.start()
    t2.start()
    t3.start()
    print('The main process is still running')
    t1.join() # optionally we may pause the main process until another process (re)joins
    t2.join()
    t3.join()
    print('Main process will only continue after the processes have (re)joined')

if __name__ == '__main__':
    main()