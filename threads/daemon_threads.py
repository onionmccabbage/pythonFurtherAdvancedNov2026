# daemon threads run continuously
# similar to what was a TSR "terminate and stay resident"
import threading
import time

def normalFn():
    '''we will call this on a normal thread'''
    print('normal thread is starting')
    time.sleep(5)
    print('normal thread is done')

def daemonFn():
    '''we will call this a a daemon thread'''
    print('Daemon thread is starting')
    while True:
        time.sleep(0.5)
        print('heartbeat.....')

def main():
    st = threading.Thread(target=normalFn)
    dt = threading.Thread(target=daemonFn, daemon=True)
    st.start()
    dt.start()
    # we do not need to join other threads but we may choose to
    st.join()
    # we never join a daemon thread

if __name__ == '__main__':
    main()