# Example of simple echo server
# www.solusipse.net

import socket
import json
import pickle


class customObject:
    def __init__(self):
        self.i = 555
        self.j = 777



def listen():
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    connection.bind(('localhost', 5555))
    connection.listen(10)
    while True:
        current_connection, address = connection.accept()
        while True:
            data = current_connection.recv(2048)
            try:

                ### JSON with object
                myObject = customObject()
                current_connection.send(json.dumps(myObject, default=lambda o: o.__dict__).encode())


                ### JSON with list
                # list
                # myList = [99,88,{'a': 3},77]
                # current_connection.send(json.dumps(myList).encode())

                # Binary with pickle
                # myObject2 = customObject()
                # zzzz = pickle.dumps(myObject2)
                # current_connection.send(zzzz)

                # Binary with list
                # myList = [99, 88]
                # current_connection.send(bytes(myList))
            except Exception as e:
                print(e)
            print(data)

if __name__ == "__main__":
    try:
        listen()
    except KeyboardInterrupt:
        pass
    print('done')