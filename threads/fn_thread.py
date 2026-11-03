from threading import Thread

# we will use these to simulate long-running operations
import random
import time

def myFn(n):
    for i in range(0,6):
        print(f'{n} is working...')
        time.sleep(random.random()*0.1 )

def main():
    '''create a number of threads each using our function'''
    t1 = Thread(target=myFn,args=(1,)) # args is always a tuple (here a one-member tuple)
    t2 = Thread(target=myFn,args=(2,)) # args is always a tuple (here a one-member tuple)
    t3 = Thread(target=myFn,args=(3,)) # args is always a tuple (here a one-member tuple)
    # at any moment we may choose to sequentialy start the threads
    t1.start()
    t2.start()
    t3.start()
    print('The main thread is still running')
    t1.join() # optionally we may pause the main thread until another thread (re)joins
    t2.join()
    t3.join()
    print('Main thread will only continue after the threads have (re)joined')

    # it is good practice to tidy up
    



if __name__ == '__main__':
    main()