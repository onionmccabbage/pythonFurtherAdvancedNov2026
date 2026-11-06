from threading import Semaphore, current_thread

sem = Semaphore()
def writeBytes(n):
    '''persist the incoming data 'n' into a byte file
    NB much data is not-textual
    Also, bytes are more efficient'''
    global sem
    print(f'Writing to bytefile from { current_thread().name }')
    with open('my_bytes', 'ab') as fout: # 'ab' will append bytes
        if type(n) == bytes:
            sem.acquire()
            fout.write(n)
            # we may choose to add a new line character
            fout.write('\n'.encode()) # make sure it is bytes
            sem.release()
        else:
            raise TypeError('Cannot work with non-byte data')
