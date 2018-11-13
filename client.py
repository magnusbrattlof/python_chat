import socket

class Client:
    def __init__(self, server, port):
        self.server = server
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection = (self.server, self.port)

    def connect(self):
        pass

port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = ('localhost', port)

s.connect(server)
data = input("Message: ")
s.send(data.encode())
print("Waiting for receive data")
response = s.recv(1024)
print(response)
s.close()
