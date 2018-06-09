import json
import socket
import pickle
import sys


class customObject:
    def __init__(self):
        self.i = 0
        self.j = 4




# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 5555)
#print >>sys.stderr, 'connecting to %s port %s' % server_address
print('connecting')
sock.connect(server_address)

try:
    
    # Send data
    message = 'This is the message.  It will be repeated.'
    #print >>sys.stderr, 'sending "%s"' % message
    print('sending')
    #sock.sendall(message)
    sock.sendall(message.encode('utf-8'))

    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    #print(1/0)
    
    #while amount_received < amount_expected:
    #data = sock.recv(16)
    data = sock.recv(2048)

    ### JSON method
    myList = json.loads(data.decode())
    print(myList)

    ### Binary with pickle
    # zzzz = pickle.loads(data)
    # nnnn = 0

    ### Binary with list
    # amount_received += len(data)
    # print >>sys.stderr, 'received "%s"' % data
    # print('received', list(data))

except Exception as e:
    print(e)

finally:
    #print >>sys.stderr, 'closing socket'
    print('closing')
    sock.close()