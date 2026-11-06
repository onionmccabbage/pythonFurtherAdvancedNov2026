import socket
import threading
from byteWriter import writeBytes

def server():
    ''' a simple socket server (a microservice)'''
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind( ('localhost', 8887) )
    server.listen() 
    #  we need a run loop
    while True:
        try:
            (client, addr) = server.accept()
            buffer = client.recv(1024) # usually read just the first bytes of the client
            # we may then decide whether to proceed
            buf_str = buffer.decode() # convert hte byte string to a normal text string
            print(f'Server received {buf_str}')
            # persist this into the byte file
            writeBytes( buffer ) # buffer is the first part of encoded data stream
            if buffer == b'quit':
                break # stop the server
            else:
                response = buffer.upper()
                client.send(response)
        except Exception as err:
            print(f'Problem {err}')

if __name__ == '__main__':
    server()