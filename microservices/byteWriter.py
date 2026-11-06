def writeBytes(n):
    '''persist the incoming data 'n' into a byte file
    NB much data is not-textual
    Also, bytes are more efficient'''
    with open('my_bytes', 'ab') as fout: # 'ab' will append bytes
        if type(n) == bytes:
            fout.write(n)
            # we may choose to add a new line character
            fout.write('\n'.encode()) # make sure it is bytes
        else:
            raise TypeError('Cannot work with non-byte data')
