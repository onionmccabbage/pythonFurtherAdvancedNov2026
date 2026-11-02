from contextlib import contextmanager
import sys

@contextmanager
def outputRedirect(newStream):
    '''redirect output to a new stream'''
    old_sdtout = sys.stdout
    sys.stdout = newStream
    yield # this lets us yield a value without ending the function
    sys.stdout = old_sdtout # put things back how they were


def main():
    '''exercise the code'''
    print('using the default output stream')
    with open('my_log.txt', 'at') as fout:
        with outputRedirect(fout):
            print('content to be redirected')
    print('normal service resumed')

if __name__ == '__main__':
    main()
