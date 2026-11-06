import asyncio
from byteWriter import writeBytes
import threading

# here the reader and the writer are microservice url-encoded interactions
async def handleRequests( reader, writer ):
    ''' this server will handle requsts from clients '''
    buffer = await reader.read(1024)
    message = 'default'
    try:
        message = buffer.decode()
    except UnicodeDecodeError as err:
        print(f'problem: P{err}')
    address = writer.get_extra_info('peername') # this will be provided by the writer object
    print(f'Server received {message} from {address}')
    t = threading.Thread(target=writeBytes, kwargs={'n':buffer.upper()})
    t.start()
    if message.lower() in ('quit', 'end', 'terminate'):
        '''terminate this server'''
        quit # stop current execution

async def main():
    '''start the service'''
    server = await asyncio.start_server(handleRequests, 'localhost', 8889)
    print('Async Server is running')
    async with server: # with will always clean up when done
        await server.serve_forever()

if __name__ == '__main__':
    asyncio.run( main() )
