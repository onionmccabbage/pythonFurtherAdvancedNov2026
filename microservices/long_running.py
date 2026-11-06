# co-routines
import time
import random

def long(_):
    # this might be I/O bound...
    time.sleep(random.random()*3) # sleep for 0-3 sec
    print(f'{_} completed')

if __name__ == '__main__':
    for _ in range(10):
        long(_) # this is proceedural takes time
        print('...')
    