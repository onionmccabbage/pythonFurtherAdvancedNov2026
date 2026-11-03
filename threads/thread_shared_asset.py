import threading
import time
import random

# here are some global assets (miht be files, db, u-servers etc.)
testsAvailable = 32
num_threads = 4

class TestRunner(threading.Thread):
    '''Emulate running tests that take time to complete'''
    testsDone = 0
    def __init__(self, i):
        threading.Thread.__init__(self)
        # if we use super() then we are obliged to pass ALL the following members
        # super().__init__(group, target, name, args, kwargs, daemon=daemon, context=context)
        self.i = i
    def run(self): # this is the method the Thread call will use
        global testsAvailable
        running = True
        while running:
            # wait for a random time
            self.randomDelay()
            # emulate running a test
            if testsAvailable <=0:
                running=False # or we ould use break
            else:
                testsAvailable -=1
                self.testsDone +=1
                # here we would run the test
        # when the loop ends...
        print(f'{self.i} completed {self.testsDone} tests')
    def randomDelay(self):
        '''sleep for a random time'''
        time.sleep(random.randint(0,4)/4) # 0, 0.25, 0.5, 0.75 sec