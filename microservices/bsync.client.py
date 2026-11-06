import asyncio
import sys

async def client(msg):
    '''an asynchronous client which will send a message to server
    NB the server need not be async, it could be a conventional socket server'''
    # convert any incoming data to bytes
    b = makeBytes(msg)
    reader, writer = await asyncio.open_connection('localhost', 8889)
    print(f'Client is sending {b}')
    # no await
    writer.write(b)
    # await for co-routine to complete
    # NB we use await for I/O bound operations
    # or anything outside the control of Python
    # typially these operations may return timeouts
    await writer.drain() # wait for the entire stream to be sent
    # no await
    writer.close()

def makeBytes(n):
    b = bytes(n)
    return b

if __name__ == '__main__':
    if len(sys.argv)>1:
        msg = ', '.join(sys.argv[1:])
    else:
        msg = range(0,60) # use bytes for the first 256 ANSII characters
    # we need to run our client
    asyncio.run( client(msg) )