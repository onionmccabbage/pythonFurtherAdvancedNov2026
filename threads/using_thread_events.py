# once a thread is started, it is completely on its own
# There is no mechanism to control it or interact other than...
# thread events

from threading import Thread, Event
import time

ev = Event() # an instance of a Thread Event

def fn(n):
    global ev
    print(f'{n} is waiting for an event')
    ev.wait() # this thread will not proceed until it receives the event
    print(f'{n} continuing after event')

def main():
    '''run several threads, then make an event'''
    thread_l = [Thread(target=fn, args=(_, )) for _ in range(0,4)]
    for t in thread_l:
        t.start()
    # pause a while on the main thread
    time.sleep(5)
    ev.set() # this broadcaasts the event to all running threads. They may choose to respond to it

if __name__ == '__main__':
    main()