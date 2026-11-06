import socket
import sys

def client():
    '''simple socket client interacting with our server'''
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect( ('localhost', 8887) )
        # if there is an extra system argument variable, send it
        msg = 'default'
        if len(sys.argv) > 1:
            msg = ', '.join(sys.argv[1:])
        # else:
        #     msg = 'default'
        # always a good idea to encode, but remember sockets will urlencode everything
        client.send( msg.encode() ) # we need to encode here
        # we may reasonably expect a response from the server
        received = client.recv(1024)
        print(f'Client received {received.decode()}')
        # we could do operations such as persist to a byte file
        client.close()
    # it is worth handling typical exceptions separately to we are able to deal with outcomes
    # handle most specific exceptions first
    except ConnectionAbortedError as err:
        print(f'Connection Aborted {err}')
    except ConnectionRefusedError as err:
        # we may have a strategy of trying again a few times
        print(f'Connection Refused {err}')
    except ConnectionError:
        # we may choose to redirect the stderr for some exceptino typesS
        print(f'Connection error {err}')
    # handle all generic exceptions last
    except Exception as err:
        print(f'Problem {err}')

if __name__ == '__main__':
    # print(sys.argv)
    client()