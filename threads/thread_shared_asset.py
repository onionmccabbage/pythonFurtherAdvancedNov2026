import threading
import time
import random

# here are some global assets (miht be files, db, u-servers etc.)
testsAvailable = 1024 # imagine this is capable of more than one concurrent access
num_threads = 64 # aim to balance number of threads with numer of tasks
# we may provide a lock to make our code thread-safe
lk = threading.RLock() # we have an instance of the Lock
sem = threading.Semaphore(4) # this allows more than one concurrent access to a resource

class TestRunner(threading.Thread):
    '''Emulate running tests that take time to complete'''
    testsDone = 0
    def __init__(self, i):
        threading.Thread.__init__(self)
        # if we use super() then we are obliged to pass ALL the following members
        # super().__init__(group, target, name, args, kwargs, daemon=daemon, context=context)
        self.i = i
        self.lk = lk # grab the lock (we will need it later)
        self.sem = sem # grab access to the semaphore
    def run(self): # this is the method the Thread call will use
        global testsAvailable
        running = True
        while running:
            # wait for a random time
            self.randomDelay()
            # emulate running a test
            # self.lk.acquire() # here we gain exclusive access to assets
            self.sem.acquire() # here we gain shared access to assets
            if testsAvailable <=0:
                running=False # or we ould use break
            else:
                testsAvailable -=1
                self.testsDone +=1
                # here we would run the test
            # self.lk.release() # make the lock available to others
            self.sem.release() # make the semaphore available to others
        # when the loop ends...
        print(f'{self.i} completed {self.testsDone} tests')
    def randomDelay(self):
        '''sleep for a random time'''
        time.sleep(random.randint(0,4)/4) # 0, 0.25, 0.5, 0.75 sec

def main():
    global num_threads
    instanceList = []
    # start a timer
    start = time.perf_counter()
    for _ in range(0, num_threads):
        tester = TestRunner(_)
        instanceList.append(tester)
        tester.start()

    # after we have started all the threads we usually choose to joni them all
    for _ in instanceList:
        _.join()
    # measure time interval
    print(f'Total time: {time.perf_counter()-start:0.4f} sec')

if __name__ == '__main__':
    main()