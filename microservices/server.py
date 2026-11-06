import socket
import threading
from byteWriter import writeBytes

def server():
    ''' a simple socket server (a microservice)'''
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind( ('localhost', 8887) )
    # liten itself is thread safe
    server.listen(4) # the backlog is how many concurrent clients we choose to handle 
    #  we need a run loop
    while True:
        try:
            (client, addr) = server.accept()
            buffer = client.recv(1024) # usually read just the first bytes of the client
            # we may then decide whether to proceed
            buf_str = buffer.decode() # convert hte byte string to a normal text string
            print(f'Server received {buf_str}')
            # persist this into the byte file on a separate thread
            # NB we would need a lock/sepahore on our byte file
            t = threading.Thread(target=writeBytes, args=(buffer,))
            # writeBytes( buffer ) # buffer is the first part of encoded data stream
            t.start() # set the byteWriter to run on a new thread
            if buffer == b'quit':
                break # stop the server
            else:
                response = buffer.upper()
                client.send(response)
        except Exception as err:
            print(f'Problem {err}')

if __name__ == '__main__':
    server()